// Sends the bare domain to www so search engines see one site, then serves the static files.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname === 'thejeremiahajayi.com') {
      url.hostname = 'www.thejeremiahajayi.com';
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  }
};
