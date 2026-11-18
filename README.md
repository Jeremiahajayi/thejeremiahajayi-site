# thejeremiahajayi.com

Static site for Jeremiah Ajayi, hosted on Cloudflare Pages.

- `dist/` is the published site. Cloudflare Pages serves this folder (no build command, output directory `dist`).
- `project/` holds the page sources exported from the design canvas.
- `export/` turns those pages into static HTML, adds SEO files, Google Tag Manager (GTM-TQCD7V7B) and the blog posts.
- `posts/` holds the blog posts migrated from Wix, kept at their original /post/ URLs.
- `tools/` holds the three interactive tools (GTM scorecard, marketing audit, category visibility audit).
- `assets/` holds the site images.

To update: change the files in `project/` (or `posts/`, `tools/`), run `./build.sh`, commit and push. Cloudflare redeploys automatically.
