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
        "subhead": "Auto-detects edges, corrects perspective, and eliminates harsh shadows in real-time.",
        "image": os.path.join(DEVICE_DIR, "real_docket_camera_scanner.png"),
        "img_offset_y": "0px",
        "callout_text": "✦ On-Device Edge Detection",
        "callout_pos": "bottom: 120px; right: -30px;"
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
        "callout_text": "✦ Zero Cloud · 100% Offline",
        "callout_pos": "bottom: 140px; left: -20px;"
    },
    {
        "id": "03_fulltext_search",
        "badge": "🔍 BLISTERING-FAST SEARCH",
        "badge_color": "#E8DEF8",
        "badge_text": "#4A4458",
        "headline": "Find Anything <span class='accent'>Instantly</span>",
        "subhead": "Full-text indexing searches through every word inside your documents in milliseconds.",
        "image": os.path.join(DEVICE_DIR, "real_docket_search_clean.png"),
        "img_offset_y": "-40px",
        "callout_text": "✦ Searches OCR Text",
        "callout_pos": "bottom: 140px; right: -20px;"
    },
    {
        "id": "04_smart_organization",
        "badge": "📁 SMART ORGANIZATION",
        "badge_color": "#D3E3FD",
        "badge_text": "#041E49",
        "headline": "Your Documents, <span class='accent'>Organized</span>",
        "subhead": "Two-column folder grid, category filter chips, and high-contrast visual thumbnails.",
        "image": os.path.join(DEVICE_DIR, "real_docket_library_with_folders.png"),
        "img_offset_y": "-40px",
        "callout_text": "✦ 2-Column Folders & Tags",
        "callout_pos": "bottom: 130px; left: -20px;"
    },
    {
        "id": "05_encrypted_backup",
        "badge": "🔒 ZERO-KNOWLEDGE BACKUP",
        "badge_color": "#FEE2E2",
        "badge_text": "#991B1B",
        "headline": "100% Private. <span class='accent'>Zero Cloud.</span>",
        "subhead": "Passphrase-encrypted backups stay on your device or go wherever you choose.",
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
        "id": "07_pdf_export",
        "badge": "📄 SEAMLESS SHARING",
        "badge_color": "#D3E3FD",
        "badge_text": "#041E49",
        "headline": "Export Searchable <span class='accent'>PDFs</span>",
        "subhead": "Share clean multi-page PDFs directly to Drive, Email, WhatsApp, or Quick Share.",
        "image": os.path.join(DEVICE_DIR, "real_docket_export_sheet.png"),
        "img_offset_y": "-40px",
        "callout_text": "✦ Native Android Share Sheet",
        "callout_pos": "bottom: 140px; right: -20px;"
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

print("All 7 Google Play Store screenshots generated successfully!")
