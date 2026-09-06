import subprocess
import os

OUTPUT_DIR = r"E:\Docket\sample_docs"
os.makedirs(OUTPUT_DIR, exist_ok=True)
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
ADB_PATH = r"C:\Users\hp\AppData\Local\Android\Sdk\platform-tools\adb.exe"

DOC_STYLE = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }
body {
  width: 1400px;
  height: 1980px;
  background: #FFFFFF;
  padding: 80px 90px;
  color: #111827;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.mono { font-family: 'JetBrains Mono', monospace; }
"""

# Document 1: Whirlpool Store Invoice
HTML_DOC_1 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{DOC_STYLE}
.header {{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  border-bottom: 3px solid #111827;
  padding-bottom: 40px;
}}
.brand-name {{
  font-size: 42px;
  font-weight: 900;
  letter-spacing: -0.03em;
  color: #0B57D0;
}}
.inv-title {{
  font-size: 56px;
  font-weight: 900;
  text-align: right;
  letter-spacing: -0.03em;
}}
.meta-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  margin: 50px 0;
}}
.label {{
  font-size: 18px;
  font-weight: 700;
  color: #6B7280;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 8px;
}}
.val {{
  font-size: 26px;
  font-weight: 600;
  color: #111827;
}}
table {{
  width: 100%;
  border-collapse: collapse;
  margin: 40px 0;
}}
th {{
  text-align: left;
  padding: 20px;
  background: #F3F4F6;
  font-size: 20px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border-bottom: 2px solid #E5E7EB;
}}
td {{
  padding: 28px 20px;
  font-size: 24px;
  font-weight: 600;
  border-bottom: 1px solid #E5E7EB;
}}
.total-box {{
  align-self: flex-end;
  width: 500px;
  background: #F9FAFB;
  border: 2px solid #E5E7EB;
  border-radius: 20px;
  padding: 30px;
}}
.total-row {{
  display: flex;
  justify-content: space-between;
  font-size: 24px;
  font-weight: 600;
  color: #4B5563;
  margin-bottom: 14px;
}}
.grand-total {{
  display: flex;
  justify-content: space-between;
  font-size: 38px;
  font-weight: 900;
  color: #0B57D0;
  border-top: 2px solid #E5E7EB;
  padding-top: 18px;
  margin-top: 14px;
}}
.footer-notes {{
  border-top: 1px solid #E5E7EB;
  padding-top: 30px;
  font-size: 18px;
  color: #6B7280;
  line-height: 1.6;
}}
</style>
</head>
<body>
  <div>
    <div class="header">
      <div>
        <div class="brand-name">WHIRLPOOL OFFICIAL STORE</div>
        <div style="font-size:22px; color:#4B5563; margin-top:8px;">Authorized Major Appliance Center #492</div>
        <div style="font-size:20px; color:#6B7280; margin-top:4px;">1400 Michigan Ave, Chicago, IL 60605</div>
      </div>
      <div>
        <div class="inv-title">INVOICE</div>
        <div class="mono" style="font-size:24px; font-weight:700; color:#0B57D0; text-align:right; margin-top:8px;">#INV-2026-8829</div>
      </div>
    </div>

    <div class="meta-grid">
      <div>
        <div class="label">Billed To</div>
        <div class="val" style="font-size:30px; font-weight:800;">Alex Morgan</div>
        <div class="val" style="font-size:22px; color:#4B5563; margin-top:4px;">742 Evergreen Terrace, Apt 4B</div>
        <div class="val" style="font-size:22px; color:#4B5563;">alex.morgan@example.com</div>
      </div>
      <div style="text-align:right;">
        <div class="label">Invoice Date</div>
        <div class="val mono">March 12, 2026</div>
        <div class="label" style="margin-top:20px;">Payment Method</div>
        <div class="val">Visa ending in **** 4921 (Authorized)</div>
      </div>
    </div>

    <table>
      <thead>
        <tr>
          <th style="width:55%;">Description</th>
          <th style="text-align:center;">Qty</th>
          <th style="text-align:right;">Unit Price</th>
          <th style="text-align:right;">Total</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <div style="font-size:26px; font-weight:800;">Whirlpool 36-inch French Door Refrigerator</div>
            <div class="mono" style="font-size:20px; color:#4B5563; margin-top:6px;">Model: WRX735SDHZ · S/N: 8829-XPS</div>
          </td>
          <td style="text-align:center;">1</td>
          <td style="text-align:right;" class="mono">$1,199.00</td>
          <td style="text-align:right; font-weight:800;" class="mono">$1,199.00</td>
        </tr>
        <tr>
          <td>
            <div style="font-size:26px; font-weight:800;">3-Year Extended Protection Warranty</div>
            <div style="font-size:20px; color:#4B5563; margin-top:6px;">Full on-site parts & labor coverage through March 2029</div>
          </td>
          <td style="text-align:center;">1</td>
          <td style="text-align:right;" class="mono">$50.00</td>
          <td style="text-align:right; font-weight:800;" class="mono">$50.00</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div>
    <div style="display:flex; justify-content:flex-end;">
      <div class="total-box">
        <div class="total-row">
          <span>Subtotal</span>
          <span class="mono">$1,249.00</span>
        </div>
        <div class="total-row">
          <span>Sales Tax (8.25%)</span>
          <span class="mono">$103.04</span>
        </div>
        <div class="grand-total">
          <span>Total Paid</span>
          <span class="mono">$1,352.04</span>
        </div>
      </div>
    </div>

    <div class="footer-notes" style="margin-top:60px;">
      <div style="font-weight:800; color:#111827; margin-bottom:6px;">WARRANTY & RETURN POLICY</div>
      <div>Retain this invoice for warranty claims. Proof of purchase required for all authorized service calls. Model and serial number must remain intact on device cabinet. Call Whirlpool Support at 1-800-253-1301 with your invoice number #INV-2026-8829.</div>
    </div>
  </div>
</body>
</html>
"""

# Document 2: Apartment Lease Agreement
HTML_DOC_2 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{DOC_STYLE}
.title-block {{
  text-align: center;
  border-bottom: 2px solid #111827;
  padding-bottom: 30px;
}}
.main-title {{
  font-size: 46px;
  font-weight: 900;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}}
.clause {{
  margin: 30px 0;
}}
.clause-title {{
  font-size: 24px;
  font-weight: 800;
  color: #111827;
  text-transform: uppercase;
  margin-bottom: 10px;
}}
.clause-text {{
  font-size: 21px;
  color: #374151;
  line-height: 1.65;
}}
.sig-box {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  margin-top: 60px;
  border-top: 2px solid #E5E7EB;
  padding-top: 40px;
}}
.sig-line {{
  border-top: 2px solid #111827;
  margin-top: 70px;
  padding-top: 10px;
  font-size: 20px;
  font-weight: 700;
}}
</style>
</head>
<body>
  <div>
    <div class="title-block">
      <div class="main-title">Residential Lease Agreement</div>
      <div style="font-size:22px; color:#4B5563; margin-top:8px;">Standard Form Apartment Lease · State of Illinois</div>
    </div>

    <div style="background:#F9FAFB; border:2px solid #E5E7EB; border-radius:18px; padding:30px; margin:40px 0;">
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:20px; font-size:22px;">
        <div><strong>LANDLORD:</strong> Metro Property Management LLC</div>
        <div><strong>TENANT:</strong> Alex Morgan</div>
        <div><strong>PREMISES:</strong> 742 Evergreen Terrace, Apt 4B</div>
        <div><strong>TERM:</strong> 12 Months (Apr 1, 2026 - Mar 31, 2027)</div>
      </div>
    </div>

    <div class="clause">
      <div class="clause-title">Section 1. Monthly Rent & Payment Terms</div>
      <div class="clause-text">Tenant agrees to pay the Landlord a monthly rent of <strong>$1,850.00 USD</strong>, due promptly on the first (1st) day of each calendar month. Payments made after the fifth (5th) day of the month are subject to an administrative late fee of $75.00 USD.</div>
    </div>

    <div class="clause">
      <div class="clause-title">Section 2. Security Deposit</div>
      <div class="clause-text">Upon signing of this Lease, Tenant has deposited with Landlord the sum of <strong>$1,850.00 USD</strong> as security for the faithful performance of all terms, covenants, and conditions of this Agreement. Said deposit shall be held in an escrow account.</div>
    </div>

    <div class="clause">
      <div class="clause-title">Section 3. Use of Premises & Utilities</div>
      <div class="clause-text">The premises shall be occupied strictly as a private single-family residence. Water, sewer, and municipal trash collection shall be furnished by Landlord. Gas and electricity shall be established in Tenant's own name prior to possession.</div>
    </div>
  </div>

  <div class="sig-box">
    <div>
      <div style="font-style:italic; font-size:32px; font-family:serif; color:#0B57D0;">David H. Keller</div>
      <div class="sig-line">Landlord Authorized Signature</div>
      <div style="font-size:18px; color:#6B7280; margin-top:4px;">Date: March 15, 2026</div>
    </div>
    <div>
      <div style="font-style:italic; font-size:32px; font-family:serif; color:#0B57D0;">Alex Morgan</div>
      <div class="sig-line">Tenant Signature</div>
      <div style="font-size:18px; color:#6B7280; margin-top:4px;">Date: March 15, 2026</div>
    </div>
  </div>
</body>
</html>
"""

# Document 3: Studio Tech Warranty Card
HTML_DOC_3 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{DOC_STYLE}
.header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #0B57D0;
  color: white;
  padding: 40px 50px;
  border-radius: 24px;
}}
.card-content {{
  margin: 50px 0;
}}
.product-box {{
  border: 3px solid #0B57D0;
  border-radius: 24px;
  padding: 40px;
  background: #F4F7FC;
  margin-bottom: 40px;
}}
.spec-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 30px;
  margin-top: 24px;
}}
</style>
</head>
<body>
  <div>
    <div class="header">
      <div>
        <div style="font-size:44px; font-weight:900; letter-spacing:-0.02em;">TECH CORP SOLUTIONS</div>
        <div style="font-size:22px; opacity:0.9; margin-top:6px;">Official Hardware Warranty & Support Certificate</div>
      </div>
      <div class="mono" style="font-size:26px; background:white; color:#0B57D0; font-weight:800; padding:12px 24px; border-radius:12px;">
        CERTIFIED
      </div>
    </div>

    <div class="card-content">
      <div class="product-box">
        <div style="font-size:20px; font-weight:800; color:#0B57D0; text-transform:uppercase; letter-spacing:0.05em;">Registered Product</div>
        <div style="font-size:38px; font-weight:900; color:#111827; margin-top:8px;">Studio Shodwe 15 9530 Developer Edition</div>

        <div class="spec-grid">
          <div>
            <div style="font-size:18px; color:#6B7280; font-weight:700; text-transform:uppercase;">Service Tag</div>
            <div class="mono" style="font-size:30px; font-weight:900; color:#0B57D0;">49B2X73</div>
          </div>
          <div>
            <div style="font-size:18px; color:#6B7280; font-weight:700; text-transform:uppercase;">Serial Number</div>
            <div class="mono" style="font-size:30px; font-weight:900; color:#111827;">8829-XPS</div>
          </div>
          <div>
            <div style="font-size:18px; color:#6B7280; font-weight:700; text-transform:uppercase;">Support Plan</div>
            <div style="font-size:24px; font-weight:800; color:#111827;">3-Year ProSupport Plus</div>
          </div>
          <div>
            <div style="font-size:18px; color:#6B7280; font-weight:700; text-transform:uppercase;">Valid Through</div>
            <div class="mono" style="font-size:24px; font-weight:800; color:#0C7A5C;">February 18, 2029</div>
          </div>
        </div>
      </div>

      <div style="font-size:26px; font-weight:800; color:#111827; margin-bottom:16px;">Coverage Terms & Entitlements</div>
      <div style="font-size:21px; color:#4B5563; line-height:1.7;">
        • 24x7 Priority technical telephone and online dispatch support.<br>
        • Next Business Day on-site hardware technician service across North America.<br>
        • Accidental damage protection including drops, liquid spills, and electrical surges.<br>
        • Retain Your Hard Drive entitlement during motherboard or chassis repairs.
      </div>
    </div>
  </div>

  <div style="border-top:2px solid #E5E7EB; padding-top:30px; display:flex; justify-content:space-between; align-items:center;">
    <div style="font-size:18px; color:#6B7280;">Support Portal: techcorp.example.com/support · Phone: 1-800-456-3355</div>
    <div class="mono" style="font-size:18px; color:#0B57D0; font-weight:700;">REGISTRATION ID: 8829-49B2-2026</div>
  </div>
</body>
</html>
"""

DOCS = [
    ("whirlpool_invoice.html", "whirlpool_invoice.png", HTML_DOC_1),
    ("lease_agreement.html", "lease_agreement.png", HTML_DOC_2),
    ("equipment_warranty.html", "equipment_warranty.png", HTML_DOC_3),
]

for html_name, png_name, content in DOCS:
    html_file = os.path.join(OUTPUT_DIR, html_name)
    png_file = os.path.join(OUTPUT_DIR, png_name)
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)
        
    subprocess.run([
        CHROME_PATH,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--virtual-time-budget=2000",
        f"--screenshot={png_file}",
        "--window-size=1400,1980",
        f"file:///{html_file.replace(os.sep, '/')}"
    ], check=True)
    print(f"Rendered {png_name}")

    # Push to phone's Pictures and Download directories
    for phone_dir in ["/sdcard/Pictures/", "/sdcard/Download/"]:
        subprocess.run([ADB_PATH, "push", png_file, phone_dir], check=True)
        # Notify Android MediaScanner so Gallery immediately sees the images
        subprocess.run([
            ADB_PATH, "shell", "am", "broadcast",
            "-a", "android.intent.action.MEDIA_SCANNER_SCAN_FILE",
            "-d", f"file://{phone_dir}{png_name}"
        ], check=True)

print("All sample documents pushed to phone successfully!")
