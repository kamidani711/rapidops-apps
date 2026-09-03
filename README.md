# apps.rapidops.io — RapidOps Apps Studio & Portfolio

Official website source code for **`apps.rapidops.io`** and all RapidOps mobile utilities (including **Docket**).

---

## 📁 Directory Structure

```text
apps.rapidops.io/
├── index.html                   # RapidOps Apps Studio & Developer Portfolio Hub
├── sitemap.xml                  # Search engine index covering root and all app pages
├── robots.txt                   # Standard crawler access rules
├── _headers                     # Security & caching headers (Cloudflare Pages / Netlify)
│
└── docket/                      # Docket — 100% On-Device Document Scanner
    ├── index.html               # High-conversion product landing page & live UI simulator
    ├── privacy.html             # Standalone, Google Play Store compliant Privacy Policy
    └── screenshots/             # 7 official 1080×2400 Play Store screenshot assets & gallery
        ├── index.html           # Interactive web gallery to preview/download all slides
        ├── 01_instant_scanner.png
        ├── 02_livetext_ocr.png
        ├── 03_fulltext_search.png
        ├── 04_smart_organization.png
        ├── 05_encrypted_backup.png
        ├── 06_lifetime_pricing.png
        └── 07_pdf_export.png
```

---

## 🚀 Deployment Instructions

### Option A: Cloudflare Pages (Recommended for custom subdomains)
1. In Cloudflare Dashboard, go to **Workers & Pages** → **Create application** → **Pages**.
2. Connect your Git repository or use direct upload:
   - **Framework preset**: `None`
   - **Build command**: *(leave blank)*
   - **Build output directory**: `.` (root of this folder)
3. Go to **Custom Domains** → Add `apps.rapidops.io`.
4. Cloudflare automatically handles SSL, caching, and CDN routing across all edge nodes worldwide.

### Option B: GitHub Pages
1. Push this folder to a dedicated repository (e.g. `github.com/your-org/apps.rapidops.io`).
2. Go to **Settings** → **Pages** → Source: `Deploy from a branch` (`main` / root `/`).
3. Under **Custom domain**, enter `apps.rapidops.io`.
4. Add a CNAME DNS record in your DNS provider:
   - Type: `CNAME`
   - Name: `apps`
   - Content: `<your-github-username>.github.io`

### Option C: Vercel or Netlify
- Drag and drop this folder into the Vercel or Netlify dashboard, then assign `apps.rapidops.io` in the Domain Settings.

---

## 🔗 Live URLs Once Deployed

| Destination | Live URL |
| :--- | :--- |
| **RapidOps Apps Studio & Portfolio** | `https://apps.rapidops.io/` |
| **Docket Product Page** | `https://apps.rapidops.io/docket/` |
| **Docket Privacy Policy** | `https://apps.rapidops.io/docket/privacy.html` |
| **Play Store Screenshot Gallery** | `https://apps.rapidops.io/docket/screenshots/index.html` |
