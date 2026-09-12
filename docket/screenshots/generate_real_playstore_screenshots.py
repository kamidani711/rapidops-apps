import os
import subprocess

OUTPUT_DIR = r"E:\Docket\play_store_screenshots"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
DEVICE_DIR = r"E:\Docket\device_screenshots"

SLIDES = [
    {
        "id": "01_instant_scanner",
        "badge": "⚡ INSTANT ML SCANNER",
        "badge_color": "#D3E3FD",
        "badge_text": "#041E49",
        "headline": "Scan Paper in <span class='accent'>Seconds</span>",
        # "in real-time" was wrong: edge detection is live in the viewfinder, but ML Kit's
        # shadow/stain cleaning pass (SCANNER_MODE_FULL) runs after capture, not on the preview.
        "subhead": "Auto-detects edges, corrects perspective, and clears harsh shadows on every capture.",
        # A real viewfinder frame with a document under the lens and the edge-detection quad
        # locked on. Captured by sampling until the preview surface actually composites into
        # screencap — it comes back black most attempts.
        "image": os.path.join(DEVICE_DIR, "real_docket_camera_scanner.png"),
        "img_offset_y": "0px",
        "callout_text": "✦ On-Device Edge Detection",
        "callout_pos": "bottom: 780px; right: -30px;"
    },
    {
        "id": "02_livetext_ocr",
        "badge": "✨ ON-DEVICE LIVE TEXT",
        "badge_color": "#E3F8F1",
        "badge_text": "#0C7A5C",
        "headline": "Tap Any Word to <span class='accent'>Copy</span>",
        "subhead": "Instant on-device OCR extracts words, totals, and addresses without cloud processing.",
        "image": os.path.join(DEVICE_DIR, "real_docket_livetext.png"),
        "img_offset_y": "-40px",
        # Was "Zero Cloud · 100% Offline". Not defensible: the merged manifest carries INTERNET
        # via ML Kit and Play Billing, the extra OCR script packs are ~25MB downloads, and
        # billing needs the network. This is the app's own account_tagline, which is both true
        # and the line the in-app privacy page is already written to support.
        "callout_text": "✦ No account · No uploads · No tracking",
        "callout_pos": "bottom: 140px; left: -20px;"
    },
    {
        "id": "03_fulltext_search",
        "badge": "🔍 SEARCH & INSTANT RESULTS",
        "badge_color": "#E8DEF8",
        "badge_text": "#4A4458",
        "headline": "Search & Find <span class='accent'>Instantly</span>",
        "subhead": "Full-text indexing searches through every word inside your documents with live highlighted OCR results.",
        "image": os.path.join(DEVICE_DIR, "real_docket_search_clean.png"),
        "img_offset_y": "-40px",
        "callout_text": "✦ Search & Highlighted Matches",
        "callout_pos": "bottom: 700px; right: -20px;"
    },
    {
        "id": "04_smart_organization",
        "badge": "📁 SMART ORGANIZATION",
        "badge_color": "#D3E3FD",
        "badge_text": "#041E49",
        "headline": "Your Documents, <span class='accent'>Organized</span>",
        # Was "PDF and image filters". Those format chips are gone from the library in the
        # current layout -- filtering by format now lives in search results, not here -- so the
        # line described controls this very screenshot does not show. What it does show is
        # folders with counts, the list/grid toggle and the sort control.
        "subhead": "Custom folders with live counts, list or grid, and sort by date, name or size.",
        "image": os.path.join(DEVICE_DIR, "real_docket_library_with_folders.png"),
        "img_offset_y": "-40px",
        # Docket has no tags. There is no tag entity, DAO or string anywhere in the app -- the
        # Room schema is Document, DocumentPage, Folder, PageOcr, PageOcrFts, ScanPage,
        # ScanSession, AnalyticsEvent. Advertising one was a listing misrepresentation.
        "callout_text": "✦ Folders, Grid & Sort",
        "callout_pos": "bottom: 130px; left: -20px;"
    },
    {
        "id": "05_encrypted_backup",
        "badge": "🔒 ZERO-KNOWLEDGE BACKUP",
        "badge_color": "#FEE2E2",
        "badge_text": "#991B1B",
        # Was "100% Private. Zero Cloud." -- and on the backup slide of all places, where the
        # app's own copy invites you to save the file to "your own Drive". The honest claim is
        # the one the app makes: the archive is encrypted with a passphrase Docket never sees,
        # so the destination does not matter.
        "headline": "Backups Only <span class='accent'>You</span> Can Open",
        "subhead": "Encrypted with a passphrase Docket never sees and cannot recover. You choose where the file goes.",
        "image": os.path.join(DEVICE_DIR, "real_docket_backup.png"),
        "img_offset_y": "-40px",
        "callout_text": "✦ AES-256 Passphrase Security",
        "callout_pos": "bottom: 140px; right: -20px;"
    },
    {
        "id": "06_lifetime_pricing",
        "badge": "💎 NO SUBSCRIPTIONS",
        "badge_color": "#FEF3C7",
        "badge_text": "#92400E",
        "headline": "One Purchase. <span class='accent'>Forever.</span>",
        "subhead": "No monthly subscriptions, no recurring fees. Core features free offline forever.",
        "image": os.path.join(DEVICE_DIR, "real_docket_unlock.png"),
        "img_offset_y": "-40px",
        "callout_text": "✦ Lifetime Ownership",
        "callout_pos": "bottom: 140px; left: -20px;"
    },
    {
        "id": "07_document_watermark",
        "badge": "🛡️ WATERMARK PROTECTION",
        "badge_color": "#EDE9FE",
        "badge_text": "#5B21B6",
        "headline": "Watermark Every <span class='accent'>Page</span>",
        "subhead": "Stamp CONFIDENTIAL, DRAFT, or custom text across your documents and exports — watermarking is part of Premium.",
        "image": os.path.join(DEVICE_DIR, "real_docket_watermark.png"),
        "img_offset_y": "-40px",
        "callout_text": "✦ Diagonal Watermark Stamp",
        "callout_pos": "bottom: 700px; left: -25px;"
    },
    {
        "id": "08_sign_document",
        "badge": "✍️ SIGN ON THE PAGE",
        "badge_color": "#E0F2FE",
        "badge_text": "#075985",
        "headline": "Sign It Without <span class='accent'>Printing</span>",
        # Signing is PremiumFeature-gated, so the slide says so rather than selling a paid
        # feature as if it were free -- the same correction already made on the export slide.
        # "travels into every PDF and image you export" is literally what PageOverlays does:
        # both export paths render the signature from the same stored placement the viewer uses.
        "subhead": "Draw your signature, drag it onto the line, and it is there in Docket and in everything you export — signing is part of Premium.",
        # A real residential lease from make_sample_docs.py, signed on its Tenant Signature line
        # through the app's own pad. Not a mockup: the tenant's printed name was blanked in the
        # sample so there was a genuinely empty line to sign.
        "image": os.path.join(DEVICE_DIR, "real_docket_signature.png"),
        "img_offset_y": "-40px",
        "callout_text": "✦ Drag it into place",
        "callout_pos": "bottom: 700px; left: -25px;"
    }
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;500;600;700;800;900&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Urbanist', sans-serif; letter-spacing: -0.02em; }

body {
  width: 1080px;
  height: 2400px;
  background: #F8FAFC;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
}

.bg-radial {
  position: absolute;
  top: -200px;
  left: 50%;
  transform: translateX(-50%);
  width: 1200px;
  height: 1100px;
  background: radial-gradient(circle, rgba(11, 87, 208, 0.15) 0%, rgba(11, 87, 208, 0.03) 60%, transparent 80%);
  z-index: 0;
}

.header-container {
  width: 960px;
  text-align: center;
  margin-top: 110px;
  margin-bottom: 50px;
  z-index: 10;
}

.badge {
  display: inline-flex;
  align-items: center;
  padding: 12px 28px;
  border-radius: 999px;
  font-size: 24px;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  margin-bottom: 24px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.04);
}

.headline {
  font-size: 72px;
  font-weight: 900;
  color: #0F172A;
  line-height: 1.14;
  margin-bottom: 18px;
}

.headline .accent {
  color: #0B57D0;
}

.subhead {
  font-size: 30px;
  font-weight: 500;
  color: #475569;
  line-height: 1.45;
  max-width: 860px;
  margin: 0 auto;
}

.phone-wrapper {
  position: relative;
  z-index: 10;
  margin-top: 20px;
}

.phone-mockup {
  width: 830px;
  height: 1780px;
  background: #0F172A;
  border-radius: 72px;
  padding: 14px;
  box-shadow: 
    0 50px 100px -20px rgba(15, 23, 42, 0.25),
    0 25px 50px -10px rgba(11, 87, 208, 0.2),
    0 0 0 1px rgba(255, 255, 255, 0.1) inset;
  position: relative;
}

.notch {
  position: absolute;
  top: 24px;
  left: 50%;
  transform: translateX(-50%);
  width: 140px;
  height: 28px;
  background: #0F172A;
  border-radius: 20px;
  z-index: 50;
  display: flex;
  align-items: center;
  justify-content: center;
}

.camera-hole {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #1E293B;
  border: 2px solid #334155;
}

.phone-screen {
  width: 100%;
  height: 100%;
  border-radius: 58px;
  overflow: hidden;
  background: #FFFFFF;
  position: relative;
}

.screen-capture {
  width: 100%;
  height: auto;
  display: block;
  transform-origin: top center;
}

.floating-pill {
  position: absolute;
  background: #0B57D0;
  color: #FFFFFF;
  font-size: 24px;
  font-weight: 800;
  padding: 16px 32px;
  border-radius: 999px;
  box-shadow: 0 20px 40px rgba(11, 87, 208, 0.4), 0 4px 10px rgba(0,0,0,0.1);
  display: flex;
  align-items: center;
  gap: 12px;
  z-index: 30;
  letter-spacing: 0.02em;
  border: 2px solid rgba(255, 255, 255, 0.4);
}
"""

for slide in SLIDES:
    img_url = f"file:///{slide['image'].replace(os.sep, '/')}"
    html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{CSS}
</style>
</head>
<body>
  <div class="bg-radial"></div>

  <div class="header-container">
    <div class="badge" style="background: {slide['badge_color']}; color: {slide['badge_text']};">
      {slide['badge']}
    </div>
    <h1 class="headline">{slide['headline']}</h1>
    <p class="subhead">{slide['subhead']}</p>
  </div>

  <div class="phone-wrapper">
    <div class="phone-mockup">
      <div class="notch">
        <div class="camera-hole"></div>
      </div>
      <div class="phone-screen">
        <img src="{img_url}" class="screen-capture" style="margin-top: {slide['img_offset_y']};" />
      </div>
    </div>
    <div class="floating-pill" style="{slide['callout_pos']}">
      {slide['callout_text']}
    </div>
  </div>
</body>
</html>
"""
    html_path = os.path.join(OUTPUT_DIR, f"{slide['id']}.html")
    png_path = os.path.join(OUTPUT_DIR, f"{slide['id']}.png")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Rendering {slide['id']}...")
    subprocess.run([
        CHROME_PATH,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--virtual-time-budget=2000",
        f"--screenshot={png_path}",
        "--window-size=1080,2400",
        f"file:///{html_path.replace(os.sep, '/')}"
    ], check=True)
    print(f"Generated: {png_path}")

print("All %d Google Play Store screenshots generated successfully!" % len(SLIDES))
