# Draft web deployment notes — AI Insurance

This repository now has a small static site in `site/`. It is still a draft, is marked `noindex`, and has not been published or deployed. Do not connect a production deployment until the product, legal language, and any use of “insurance” have been reviewed and the owner explicitly chooses to publish.

## Recommended: Cloudflare Pages from GitHub

Cloudflare Pages can connect directly to a GitHub repository; GitHub Pages does not need to sit in front of Cloudflare. For this plain HTML site, use no framework and leave the build command blank. Set the output directory to `site`.

- If this folder is its own GitHub repository: root directory `.`; output directory `site`.
- If deploying from the combined draft bundle repository: root directory `ai-insurance`; output directory `site`.
- The connected production branch should only be selected when publishing is authorized. Cloudflare Pages Git integration can deploy changes automatically after it is connected.

## Alternative: Cloudflare Workers Static Assets

`wrangler.jsonc` is a prepared static-assets configuration. From this repository root, a future preview can be run with `npx wrangler dev --config wrangler.jsonc`. A real deployment would use `npx wrangler deploy --config wrangler.jsonc`; that command has intentionally not been run. Review the project name and account/domain settings first.

## GitHub Pages alternative

For a separate GitHub Pages copy, use a GitHub Actions workflow that publishes the contents of `site/`, or move the chosen static output into the supported publishing source. No auto-deploy workflow is included here, to avoid publishing this draft accidentally. Relative HTML, CSS, image, and favicon paths are used so the files also work under a repository subpath.

## Contents

- `site/index.html` — draft landing page, including an SVG favicon link.
- `site/styles.css` — responsive styling.
- `site/assets/` — favicon and comedic promotional illustrations.
- `wrangler.jsonc` — optional Workers Static Assets configuration.
