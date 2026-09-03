import subprocess
import os

OUTPUT_DIR = r"E:\Docket\play_store_screenshots"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

COMMON_STYLE = """
@import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;500;600;700;800;900&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Urbanist', sans-serif; letter-spacing: -0.02em; }
body {
  width: 1080px;
  height: 2400px;
  background: #F4F7FC;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.bg-glow {
  position: absolute;
  top: -150px;
  left: 50%;
  transform: translateX(-50%);
  width: 1100px;
  height: 900px;
  background: radial-gradient(circle, rgba(11, 87, 208, 0.12) 0%, rgba(11, 87, 208, 0.02) 60%, transparent 80%);
  z-index: 0;
}

.header-box {
  width: 1000px;
  text-align: center;
  margin-top: 130px;
  margin-bottom: 60px;
  z-index: 10;
}
.tag-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 24px;
  border-radius: 999px;
  background: #D3E3FD;
  color: #041E49;
  font-size: 24px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 26px;
}
.tag-badge.mint {
  background: #E3F8F1;
  color: #0C7A5C;
}
.headline {
  font-size: 76px;
  font-weight: 900;
  color: #191C20;
  line-height: 1.12;
  margin-bottom: 20px;
}
.headline span.accent {
  color: #0B57D0;
}
.subhead {
  font-size: 34px;
  font-weight: 600;
  color: #565E71;
  line-height: 1.4;
  max-width: 920px;
  margin: 0 auto;
}

.phone-mockup {
  width: 860px;
  height: 1740px;
  background: #FFFFFF;
  border-radius: 90px;
  padding: 16px;
  box-shadow: 0 45px 90px -20px rgba(15, 23, 42, 0.2), 0 0 60px -10px rgba(11, 87, 208, 0.18);
  border: 10px solid #CBD5E1;
  position: relative;
  z-index: 10;
}
.phone-screen {
  width: 100%;
  height: 100%;
  background: #FFFFFF;
  border-radius: 74px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  position: relative;
  border: 2px solid #E2E8F0;
}

.status-bar {
  height: 65px;
  padding: 0 45px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 24px;
  font-weight: 800;
  color: #191C20;
  background: #FFFFFF;
}
.punch-hole {
  width: 24px;
  height: 24px;
  background: #000000;
  border-radius: 50%;
}
"""

# -------------------------------------------------------------
# 1. Authentic LibraryScreen.kt
# -------------------------------------------------------------
HTML_SCREEN_1 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{COMMON_STYLE}

.top-app-bar {{
  height: 90px;
  padding: 0 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #FFFFFF;
}}
.top-title {{
  font-size: 42px;
  font-weight: 900;
  color: #191C20;
}}
.top-actions {{
  display: flex;
  align-items: center;
  gap: 24px;
  color: #565E71;
  font-size: 32px;
}}

.search-bar {{
  margin: 14px 32px 18px;
  background: #FAFAFA;
  border: 2px solid #EEEEEE;
  border-radius: 36px;
  padding: 22px 28px;
  display: flex;
  align-items: center;
  gap: 18px;
  font-size: 26px;
  color: #565E71;
  font-weight: 600;
}}

.chips-scroll {{
  padding: 0 32px;
  display: flex;
  gap: 14px;
  margin-bottom: 20px;
}}
.m3-chip {{
  padding: 12px 28px;
  border-radius: 999px;
  font-size: 24px;
  font-weight: 800;
  background: #FAFAFA;
  border: 2px solid #EEEEEE;
  color: #565E71;
}}
.m3-chip.selected {{
  background: #0B57D0;
  border-color: #0B57D0;
  color: #FFFFFF;
}}

.folders-scroll {{
  padding: 0 32px;
  display: flex;
  gap: 16px;
  margin-bottom: 24px;
}}
.folder-pill {{
  padding: 14px 26px;
  background: #F4F7FC;
  border: 2px solid #D3E3FD;
  border-radius: 20px;
  font-size: 24px;
  font-weight: 800;
  color: #041E49;
  display: flex;
  align-items: center;
  gap: 12px;
}}

.doc-list {{
  padding: 0 32px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}}
.doc-card {{
  padding: 22px 24px;
  background: #FAFAFA;
  border: 2px solid #EEEEEE;
  border-radius: 28px;
  display: flex;
  align-items: center;
  gap: 22px;
}}
.thumb-box {{
  width: 92px;
  height: 122px;
  background: #FFFFFF;
  border: 2px solid #E2E8F0;
  border-radius: 16px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0 4px 10px rgba(0,0,0,0.04);
}}
.badge-pdf {{
  background: #FF6B67;
  color: white;
  font-size: 14px;
  font-weight: 900;
  padding: 4px 8px;
  border-radius: 6px;
  align-self: flex-start;
}}
.doc-info {{
  flex: 1;
}}
.doc-name {{
  font-size: 28px;
  font-weight: 800;
  color: #191C20;
  margin-bottom: 6px;
}}
.doc-sub {{
  font-size: 22px;
  color: #565E71;
  font-weight: 600;
  margin-bottom: 10px;
}}
.ocr-pill {{
  display: inline-flex;
  padding: 6px 14px;
  border-radius: 8px;
  background: #E3F8F1;
  color: #0C7A5C;
  font-size: 20px;
  font-weight: 800;
}}

.scan-fab {{
  position: absolute;
  bottom: 48px;
  right: 44px;
  background: #0B57D0;
  color: white;
  padding: 24px 40px;
  border-radius: 999px;
  display: flex;
  align-items: center;
  gap: 16px;
  font-size: 30px;
  font-weight: 900;
  box-shadow: 0 16px 36px rgba(11, 87, 208, 0.4);
}}
</style>
</head>
<body>
  <div class="bg-glow"></div>
  
  <div class="header-box">
    <div class="tag-badge">⚡ 100% On-Device · Zero Cloud Sync</div>
    <h1 class="headline">The Offline Scanner That <span class="accent">Protects Privacy</span></h1>
    <p class="subhead">No accounts. No server uploads. Every scan and OCR runs directly on your phone's silicon.</p>
  </div>

  <div class="phone-mockup">
    <div class="phone-screen">
      <div class="status-bar">
        <span>09:41</span>
        <div class="punch-hole"></div>
        <span>5G · 100%</span>
      </div>

      <div class="top-app-bar">
        <span class="top-title">Docket</span>
        <div class="top-actions">
          <span>田</span>
          <span>⚙️</span>
        </div>
      </div>

      <div class="search-bar">
        <svg width="28" height="28" fill="none" stroke="#0B57D0" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        <span>Search documents & scanned text...</span>
      </div>

      <div class="chips-scroll">
        <div class="m3-chip selected">All (148)</div>
        <div class="m3-chip">PDF (112)</div>
        <div class="m3-chip">Images (36)</div>
      </div>

      <div class="folders-scroll">
        <div class="folder-pill">📁 Household (34)</div>
        <div class="folder-pill">📁 Tax 2026 (21)</div>
        <div class="folder-pill">+ New</div>
      </div>

      <div class="doc-list">
        <div class="doc-card">
          <div class="thumb-box">
            <div style="height:6px; background:#191C20; border-radius:3px;"></div>
            <div class="badge-pdf">PDF</div>
          </div>
          <div class="doc-info">
            <div class="doc-name">Whirlpool fridge receipt</div>
            <div class="doc-sub">12 Mar 2026 · 2 pages · 1.4 MB</div>
            <div class="ocr-pill">OCR: Total $1,249.00 · Warranty 2029</div>
          </div>
        </div>

        <div class="doc-card">
          <div class="thumb-box">
            <div style="height:6px; background:#191C20; border-radius:3px;"></div>
            <div class="badge-pdf" style="background:#0B57D0;">PDF</div>
          </div>
          <div class="doc-info">
            <div class="doc-name">Apartment lease agreement</div>
            <div class="doc-sub">09 Mar 2026 · 4 pages · 3.8 MB</div>
            <div class="ocr-pill" style="background:#D3E3FD; color:#041E49;">OCR: Signed Tenant Lease Terms</div>
          </div>
        </div>

        <div class="doc-card">
          <div class="thumb-box">
            <div style="height:6px; background:#191C20; border-radius:3px;"></div>
            <div class="badge-pdf" style="background:#8A5300;">PDF</div>
          </div>
          <div class="doc-info">
            <div class="doc-name">Dell XPS warranty card</div>
            <div class="doc-sub">04 Mar 2026 · 1 page · 840 KB</div>
            <div class="ocr-pill">OCR: S/N 8829-XPS</div>
          </div>
        </div>
      </div>

      <div class="scan-fab">
        <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2.8" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/><path stroke-linecap="round" stroke-linejoin="round" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
        <span>Scan</span>
      </div>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# 2. Authentic DocumentDetailScreen.kt
# -------------------------------------------------------------
HTML_SCREEN_2 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{COMMON_STYLE}

.detail-top-bar {{
  height: 85px;
  padding: 0 28px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #EEEEEE;
}}
.back-btn {{
  font-size: 34px;
  color: #191C20;
  font-weight: 700;
}}
.top-menu {{
  display: flex;
  gap: 20px;
  font-size: 28px;
  color: #565E71;
}}

.detail-header {{
  padding: 26px 32px 18px;
}}
.detail-title {{
  font-size: 38px;
  font-weight: 900;
  color: #191C20;
  margin-bottom: 8px;
}}
.detail-meta {{
  font-size: 22px;
  color: #565E71;
  font-weight: 600;
}}

.action-row {{
  padding: 0 32px 20px;
  display: flex;
  gap: 14px;
}}
.detail-btn {{
  padding: 14px 22px;
  background: #F4F7FC;
  border: 2px solid #D3E3FD;
  border-radius: 20px;
  font-size: 22px;
  font-weight: 800;
  color: #0B57D0;
  display: flex;
  align-items: center;
  gap: 10px;
}}
.detail-btn.primary {{
  background: #0B57D0;
  border-color: #0B57D0;
  color: #FFFFFF;
}}

.page-scroll {{
  padding: 0 32px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}}
.page-card {{
  background: #FFFFFF;
  border: 2px solid #E2E8F0;
  border-radius: 32px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.06);
  padding: 32px;
  position: relative;
}}
.page-badge {{
  position: absolute;
  top: 24px;
  right: 24px;
  background: #F1F5F9;
  color: #565E71;
  font-size: 18px;
  font-weight: 800;
  padding: 6px 16px;
  border-radius: 999px;
}}
.ocr-box {{
  border: 2px solid rgba(11, 87, 208, 0.3);
  background: rgba(211, 227, 253, 0.35);
  border-radius: 8px;
  padding: 6px 12px;
  margin: 8px 0;
}}
</style>
</head>
<body>
  <div class="bg-glow"></div>

  <div class="header-box">
    <div class="tag-badge">📄 Page Inspector & OCR</div>
    <h1 class="headline">Continuous <span class="accent">Document Viewer</span></h1>
    <p class="subhead">Full-resolution continuous page scrolling, selectable OCR text layers, and instant multi-page export.</p>
  </div>

  <div class="phone-mockup">
    <div class="phone-screen" style="background:#FAFAFA;">
      <div class="status-bar">
        <span>09:41</span>
        <div class="punch-hole"></div>
        <span>5G · 100%</span>
      </div>

      <div class="detail-top-bar">
        <span class="back-btn">←</span>
        <span style="font-size:26px; font-weight:800; color:#565E71;">Document Details</span>
        <div class="top-menu">
          <span>✏️</span>
          <span>🗑️</span>
        </div>
      </div>

      <div class="detail-header">
        <div class="detail-title">Whirlpool fridge receipt</div>
        <div class="detail-meta">Scanned 12 Mar 2026 · 2 pages · 1.4 MB · Folder: Household</div>
      </div>

      <div class="action-row">
        <div class="detail-btn primary">
          <span>📤</span>
          <span>Export PDF</span>
        </div>
        <div class="detail-btn">
          <span>📋</span>
          <span>Copy Text</span>
        </div>
        <div class="detail-btn">
          <span>+</span>
          <span>Add Page</span>
        </div>
      </div>

      <div class="page-scroll">
        <div class="page-card">
          <div class="page-badge">Page 1 of 2</div>
          <div style="font-size:26px; font-weight:900; color:#191C20; margin-bottom:12px;">WHIRLPOOL OFFICIAL STORE</div>
          <div style="font-size:20px; color:#565E71; font-family:monospace; margin-bottom:18px;">TRANSACTION ID: 2026-0312-8829</div>
          
          <div class="ocr-box">
            <span style="font-size:18px; font-weight:800; color:#0B57D0;">[OCR Text Layer Detected]</span>
            <div style="font-size:22px; font-weight:700; color:#191C20; margin-top:4px;">Item: WRX735SDHZ French Door Refrigerator</div>
          </div>

          <div style="height:10px; background:#EEEEEE; border-radius:5px; margin:16px 0 10px; width:92%;"></div>
          <div style="height:10px; background:#EEEEEE; border-radius:5px; margin-bottom:10px; width:78%;"></div>
          <div style="height:10px; background:#EEEEEE; border-radius:5px; margin-bottom:24px; width:85%;"></div>

          <div style="border-top:2px dashed #E2E8F0; padding-top:16px; display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:22px; font-weight:800; color:#565E71;">Total Paid</span>
            <span style="font-size:32px; font-weight:900; color:#0B57D0;">$1,249.00</span>
          </div>
        </div>
      </div>

    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# 3. Authentic Full-Text Search in LibraryScreen.kt
# -------------------------------------------------------------
HTML_SCREEN_3 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{COMMON_STYLE}

.search-active-bar {{
  margin: 18px 32px 20px;
  background: #FFFFFF;
  border: 3px solid #0B57D0;
  border-radius: 36px;
  padding: 20px 28px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 10px 26px rgba(11, 87, 208, 0.15);
}}
.search-query {{
  display: flex;
  align-items: center;
  gap: 16px;
  font-size: 28px;
  font-weight: 800;
  color:#191C20;
}}
.match-badge {{
  padding: 6px 18px;
  border-radius: 999px;
  background: #E3F8F1;
  color: #0C7A5C;
  font-size: 20px;
  font-weight: 900;
}}

.result-card {{
  padding: 26px;
  background: #FFFFFF;
  border: 2px solid #E2E8F0;
  border-radius: 28px;
  margin: 0 32px 18px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.03);
}}
.result-head {{
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 12px;
}}
.tag-type {{
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: #0B57D0;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 900;
}}
.match-snippet {{
  background: #FFF3E1;
  border-left: 5px solid #8A5300;
  padding: 14px 18px;
  border-radius: 12px;
  font-size: 22px;
  color: #191C20;
  line-height: 1.45;
}}
.matched-word {{
  background: #FFD599;
  font-weight: 900;
  color: #8A5300;
  padding: 2px 6px;
  border-radius: 4px;
}}
</style>
</head>
<body>
  <div class="bg-glow"></div>

  <div class="header-box">
    <div class="tag-badge">🔍 Deep In-Document Search</div>
    <h1 class="headline">Search By What A <span class="accent">Document Says</span></h1>
    <p class="subhead">Type any serial number, price, clause, or date. Find the exact page instantly without manual tagging.</p>
  </div>

  <div class="phone-mockup">
    <div class="phone-screen" style="background:#F8FAFC;">
      <div class="status-bar">
        <span>09:41</span>
        <div class="punch-hole"></div>
        <span>5G · 100%</span>
      </div>

      <div class="search-active-bar">
        <div class="search-query">
          <svg width="30" height="30" fill="none" stroke="#0B57D0" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          <span>"serial number 8829"</span>
        </div>
        <div class="match-badge">2 MATCHES</div>
      </div>

      <div style="padding: 0 36px 16px; font-size:22px; font-weight:800; color:#565E71;">
        Matching Documents in Library
      </div>

      <div class="result-card">
        <div class="result-head">
          <div class="tag-type" style="background:#FF6B67;">PDF</div>
          <div>
            <div style="font-size:28px; font-weight:900; color:#191C20;">Dell XPS Warranty Card.pdf</div>
            <div style="font-size:20px; color:#565E71;">Page 1 · Matched in text layer</div>
          </div>
        </div>
        <div class="match-snippet">
          "...Service Tag: 49B2X · <span class="matched-word">Serial Number 8829</span>-XPS · Registered under 3 Year On-Site Hardware Warranty..."
        </div>
      </div>

      <div class="result-card">
        <div class="result-head">
          <div class="tag-type">PDF</div>
          <div>
            <div style="font-size:28px; font-weight:900; color:#191C20;">Whirlpool Fridge Invoice.pdf</div>
            <div style="font-size:20px; color:#565E71;">Page 2 · Matched in text layer</div>
          </div>
        </div>
        <div class="match-snippet">
          "...Factory Unit ID: US-MI-<span class="matched-word">8829</span>-A · Certified by Whirlpool Appliance Division..."
        </div>
      </div>

    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# 4. Authentic ExportSheet.kt
# -------------------------------------------------------------
HTML_SCREEN_4 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{COMMON_STYLE}

.sheet-modal {{
  margin: auto 0 0;
  background: #FFFFFF;
  border-top-left-radius: 48px;
  border-top-right-radius: 48px;
  padding: 36px 36px 48px;
  box-shadow: 0 -20px 60px rgba(0,0,0,0.15);
  border-top: 2px solid #E2E8F0;
}}
.sheet-handle {{
  width: 60px;
  height: 6px;
  background: #CBD5E1;
  border-radius: 3px;
  margin: 0 auto 28px;
}}
.format-tile {{
  padding: 24px;
  background: #FAFAFA;
  border: 2px solid #EEEEEE;
  border-radius: 24px;
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 14px;
}}
.format-tile.active {{
  background: #D3E3FD;
  border-color: #0B57D0;
}}
.tile-icon {{
  width: 54px;
  height: 54px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  font-weight: 900;
  color: white;
}}
.btn-export {{
  margin-top: 24px;
  background: #0B57D0;
  color: white;
  padding: 24px;
  border-radius: 999px;
  font-size: 28px;
  font-weight: 900;
  text-align: center;
  box-shadow: 0 12px 28px rgba(11, 87, 208, 0.35);
}}
</style>
</head>
<body>
  <div class="bg-glow"></div>

  <div class="header-box">
    <div class="tag-badge">📄 Export Options</div>
    <h1 class="headline">Export Pro-Grade <span class="accent">Searchable PDFs</span></h1>
    <p class="subhead">Select, copy, and search text in any PDF reader. Embedded invisible OCR text layer with zero cloud sync.</p>
  </div>

  <div class="phone-mockup">
    <div class="phone-screen" style="background:#E2E8F0;">
      <div class="status-bar" style="background:#E2E8F0;">
        <span>09:41</span>
        <div class="punch-hole"></div>
        <span>5G · 100%</span>
      </div>

      <div style="flex:1; padding:32px; opacity:0.35;">
        <div style="height:180px; background:white; border-radius:24px; margin-bottom:20px;"></div>
        <div style="height:180px; background:white; border-radius:24px;"></div>
      </div>

      <div class="sheet-modal">
        <div class="sheet-handle"></div>
        
        <div style="font-size:32px; font-weight:900; color:#191C20; margin-bottom:8px;">Export Document</div>
        <div style="font-size:22px; color:#565E71; margin-bottom:24px;">Whirlpool fridge receipt (2 pages)</div>

        <div class="format-tile active">
          <div class="tile-icon" style="background:#0B57D0;">PDF</div>
          <div style="flex:1;">
            <div style="font-size:26px; font-weight:800; color:#041E49;">Searchable PDF</div>
            <div style="font-size:20px; color:#565E71;">Embedded invisible OCR text layer</div>
          </div>
          <span style="font-size:28px; color:#0B57D0;">✓</span>
        </div>

        <div class="format-tile">
          <div class="tile-icon" style="background:#565E71;">JPG</div>
          <div style="flex:1;">
            <div style="font-size:26px; font-weight:800; color:#191C20;">Original Images (ZIP)</div>
            <div style="font-size:20px; color:#565E71;">Full resolution JPEG per page</div>
          </div>
        </div>

        <div class="format-tile">
          <div class="tile-icon" style="background:#0C7A5C;">TXT</div>
          <div style="flex:1;">
            <div style="font-size:26px; font-weight:800; color:#191C20;">Plain OCR Text</div>
            <div style="font-size:20px; color:#565E71;">Raw extracted text without images</div>
          </div>
        </div>

        <div class="btn-export">Share or Save PDF</div>
      </div>

    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# 5. Authentic BackupScreen.kt + UnlockScreen.kt
# -------------------------------------------------------------
HTML_SCREEN_5 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{COMMON_STYLE}

.backup-top-bar {{
  height: 85px;
  padding: 0 32px;
  display: flex;
  align-items: center;
  gap: 20px;
  border-bottom: 1px solid #EEEEEE;
}}
.docket-section-card {{
  margin: 0 32px 24px;
  background: #FFFFFF;
  border: 2px solid #EEEEEE;
  border-radius: 28px;
  padding: 28px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.03);
}}
.card-header {{
  font-size: 28px;
  font-weight: 900;
  color: #191C20;
  margin-bottom: 12px;
}}
.m3-input {{
  width: 100%;
  border: 2px solid #CBD5E1;
  border-radius: 16px;
  padding: 18px 20px;
  font-size: 24px;
  margin-bottom: 16px;
  color: #191C20;
  background: #FAFAFA;
}}
.primary-btn {{
  background: #0B57D0;
  color: white;
  padding: 20px;
  border-radius: 999px;
  font-size: 24px;
  font-weight: 800;
  text-align: center;
  width: 100%;
}}
.unlock-strip {{
  margin: 0 32px;
  background: linear-gradient(135deg, #0B57D0, #0842A0);
  border-radius: 28px;
  padding: 28px;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 16px 36px rgba(11, 87, 208, 0.3);
}}
</style>
</head>
<body>
  <div class="bg-glow"></div>

  <div class="header-box">
    <div class="tag-badge mint">🔒 Local Backup & Lifetime License</div>
    <h1 class="headline">Your Scans. <span class="accent">Under Your Key.</span></h1>
    <p class="subhead">Zero-knowledge AES encrypted local backups. Buy once forever with no recurring subscriptions.</p>
  </div>

  <div class="phone-mockup">
    <div class="phone-screen" style="background:#F8FAFC;">
      <div class="status-bar">
        <span>09:41</span>
        <div class="punch-hole"></div>
        <span>5G · 100%</span>
      </div>

      <div class="backup-top-bar">
        <span style="font-size:32px; color:#191C20;">←</span>
        <span style="font-size:32px; font-weight:900; color:#191C20;">Encrypted Backup</span>
      </div>

      <div style="padding: 20px 32px 16px; font-size:22px; color:#565E71; line-height:1.4;">
        Backups are encrypted on-device with your passphrase. Store anywhere without cloud lock-in.
      </div>

      <div class="docket-section-card">
        <div class="card-header">Create Encrypted Backup</div>
        <input class="m3-input" type="password" value="••••••••••••" placeholder="Enter passphrase" />
        <input class="m3-input" type="password" value="••••••••••••" placeholder="Confirm passphrase" />
        <div class="primary-btn">Create & Export Backup</div>
      </div>

      <div class="unlock-strip">
        <div>
          <div style="font-size:20px; font-weight:800; opacity:0.85; text-transform:uppercase;">Lifetime License</div>
          <div style="font-size:38px; font-weight:900;">$14.99 <span style="font-size:22px; font-weight:600; opacity:0.85;">one-time</span></div>
        </div>
        <div style="background:white; color:#0B57D0; font-size:20px; font-weight:900; padding:10px 22px; border-radius:999px;">
          No Subscriptions
        </div>
      </div>

    </div>
  </div>
</body>
</html>
"""

SCREENS = [
    ("01_library_offline.html", "01_library_offline.png", HTML_SCREEN_1),
    ("02_smart_scan_ocr.html", "02_smart_scan_ocr.png", HTML_SCREEN_2),
    ("03_fulltext_search.html", "03_fulltext_search.png", HTML_SCREEN_3),
    ("04_pro_pdf_export.html", "04_pro_pdf_export.png", HTML_SCREEN_4),
    ("05_encrypted_backup_pricing.html", "05_encrypted_backup_pricing.png", HTML_SCREEN_5),
]

for html_file, png_file, content in SCREENS:
    html_path = os.path.join(OUTPUT_DIR, html_file)
    png_path = os.path.join(OUTPUT_DIR, png_file)
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--virtual-time-budget=2500",
        f"--screenshot={png_path}",
        "--window-size=1080,2400",
        f"file:///{html_path.replace(os.sep, '/')}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(f"Generated {png_file}: status={res.returncode}")
