// Sends the bare domain to www so search engines see one site, serves the WordPress blog at /blog,
// then serves the static files.
//
// The blog runs on WordPress at Hostinger (wp.thejeremiahajayi.com, hidden from search engines).
// Requests to www.thejeremiahajayi.com/blog/... are fetched from there with the /blog prefix removed.
// WordPress's wp-config.php restores the prefix and treats https://www.thejeremiahajayi.com/blog as its address.
//
// BLOG_LIVE = false: during setup the static Writing page keeps /blog/ itself; everything below it
// (wp-admin, wp-login.php, wp-content, previews) goes to WordPress.
// BLOG_LIVE = true: /blog/ itself is WordPress too.
const BLOG_LIVE = false;
const WP_ORIGIN = 'https://wp.thejeremiahajayi.com';
const TEXT_TYPES = /text\/|javascript|json|xml/;

// Turn any link to the hidden origin into its public /blog address. Links that already carry /blog
// (WordPress builds them from its /blog address) keep a single /blog. Handles JSON-escaped slashes too.
const ORIGIN_RE = /(https?:)?(\/\/|\\\/\\\/)wp\.thejeremiahajayi\.com((?:\/|\\\/)blog(?=\/|\\\/|["'?#\s<>]|$))?/g;
function toPublic(s) {
  return s.replace(ORIGIN_RE, (m, scheme, slashes) => {
    const esc = slashes !== '//';
    const sl = esc ? '\\/\\/' : '//';
    const b = esc ? '\\/blog' : '/blog';
    return (scheme ? 'https:' : '') + sl + 'www.thejeremiahajayi.com' + b;
  });
}

function isBlogPath(pathname) {
  if (pathname !== '/blog' && !pathname.startsWith('/blog/')) return false;
  if (!BLOG_LIVE && (pathname === '/blog' || pathname === '/blog/' || pathname === '/blog/index.html')) return false;
  return true;
}

async function proxyBlog(request, url) {
  const target = new URL(WP_ORIGIN);
  target.pathname = url.pathname.replace(/^\/blog/, '') || '/';
  target.search = url.search;

  const headers = new Headers(request.headers);
  headers.set('X-Forwarded-Host', 'www.thejeremiahajayi.com');
  headers.set('X-Forwarded-Proto', 'https');
  headers.delete('Accept-Encoding');

  const init = { method: request.method, headers, redirect: 'manual' };
  if (!['GET', 'HEAD'].includes(request.method)) init.body = request.body;
  const res = await fetch(target.toString(), init);

  const out = new Headers(res.headers);
  const loc = out.get('Location');
  if (loc) out.set('Location', toPublic(loc));
  // Cookies belong to www.thejeremiahajayi.com, never the hidden origin.
  const cookies = res.headers.getSetCookie ? res.headers.getSetCookie() : [];
  if (cookies.length) {
    out.delete('Set-Cookie');
    for (const c of cookies) out.append('Set-Cookie', c.replace(/;\s*domain=[^;]*/i, ''));
  }
  // The origin marks direct visits noindex; the public copy is indexable.
  out.delete('X-Robots-Tag');

  const type = out.get('Content-Type') || '';
  if (TEXT_TYPES.test(type) && res.body) {
    const text = toPublic(await res.text());
    out.delete('Content-Length');
    return new Response(text, { status: res.status, statusText: res.statusText, headers: out });
  }
  return new Response(res.body, { status: res.status, statusText: res.statusText, headers: out });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname === 'thejeremiahajayi.com') {
      url.hostname = 'www.thejeremiahajayi.com';
      return Response.redirect(url.toString(), 301);
    }
    if (isBlogPath(url.pathname)) return proxyBlog(request, url);
    return env.ASSETS.fetch(request);
  }
};

export { isBlogPath, toPublic };
