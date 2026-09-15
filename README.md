# apps.rapidops.io — RapidOps Apps Studio & Portfolio

Official website source code for **`apps.rapidops.io`** and all RapidOps mobile utilities (including **Docket** and **Chit**).

---

## 📁 Directory Structure

```text
apps.rapidops.io/
├── index.html                   # RapidOps Apps Studio & Developer Portfolio Hub
├── sitemap.xml                  # Search engine index covering root and all app pages
├── robots.txt                   # Standard crawler access rules
├── _headers                     # Security & caching headers (Cloudflare Pages / Netlify)
│
├── docket/                      # Docket — 100% On-Device Document Scanner
│   ├── index.html               # High-conversion product landing page & live UI simulator
│   ├── privacy.html             # Standalone, Google Play Store compliant Privacy Policy
│   └── screenshots/             # 8 official 1080×2160 Play Store screenshot assets & gallery
│       ├── index.html           # Interactive web gallery to preview/download all slides
│       ├── 01_instant_scanner.png
│       ├── 02_livetext_ocr.png
│       ├── 03_fulltext_search.png
│       ├── 04_smart_organization.png
│       ├── 05_encrypted_backup.png
│       ├── 06_lifetime_pricing.png
│       ├── 07_document_watermark.png
│       └── 08_sign_document.png
│
└── chit/                        # Chit — Offline Receipt Scanner & Expense Tracker
    ├── index.html                # Product landing page
    ├── privacy.html              # Google Play Store compliant Privacy Policy
    ├── terms.html                # Terms of Service
    ├── play-store-slides.html    # Play Store marketing asset gallery
    ├── LISTING_METADATA.md       # Play Store listing copy & submission checklist
    ├── downloads/chit-v1.0.0.apk # Direct-download signed release APK (no Play Store listing yet)
    ├── graphics/                 # Play Store icon, feature graphic & 6 phone screenshot slides
    └── assets/                   # Landing page images (icon, feature graphic, in-app screenshots)
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
| **Docket Privacy Policy** | `https://apps.rapidops.io/docket/privacy` |
| **Play Store Screenshot Gallery** | `https://apps.rapidops.io/docket/screenshots/` |
| **Chit Product Page** | `https://apps.rapidops.io/chit/` |
| **Chit Privacy Policy** | `https://apps.rapidops.io/chit/privacy` |
| **Chit Terms of Service** | `https://apps.rapidops.io/chit/terms` |
| **Chit Direct APK Download** | `https://apps.rapidops.io/chit/downloads/chit-v1.0.0.apk` |
