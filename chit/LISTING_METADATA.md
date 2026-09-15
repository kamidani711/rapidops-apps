# Google Play Store Listing & Submission Package
**App Name:** Chit: Receipt Scanner & OCR  
**Package Name:** `io.rapidops.chit`  
**Version:** `1.0.0` | **VersionCode:** `1`  
**Target SDK:** Android 16 (API 36) / Minimum SDK: Android 7.0 (API 24)  
**Binary Type:** Android App Bundle (`.aab`) & Signed Release APK (`.apk`)

---

## 1. Store Listing Copy & Text Assets

### App Title (Max 30 characters)
```text
Chit: Receipt Scanner & OCR
```
*(Exact count: 27 characters)*

---

### Short Description (Max 80 characters)
```text
Fast, private offline receipt scanner, smart OCR, and monthly expense tracker.
```
*(Exact count: 79 characters)*

---

### Full Description (Formatted for Google Play Console, Max 4000 characters)
```text
Take control of your spending without sacrificing your personal privacy. Chit is a fast, offline-first receipt scanner and monthly expense manager built for individuals, freelancers, and small business owners who demand accuracy, simplicity, and complete data ownership.

Unlike other expense tracking apps that force you to create an account, pay monthly subscriptions, and upload your financial receipts to third-party cloud servers, Chit runs 100% locally on your phone. Your receipts, merchants, amounts, and budgeting numbers never leave your device.

📸 INSTANT ON-DEVICE RECEIPT SCANNING
• Point your camera at any paper receipt or invoice with built-in flashlight toggle.
• Import digital receipts, bills, and screenshots directly from your photo gallery.
• High-performance optical character recognition (OCR) extracts text and amounts in under a second.
• Automatic detection of merchant name, receipt date, tax, and total.
• No internet connection required — scan anytime, anywhere, even on airplanes or in remote locations.

📊 SMART EXPENSE TRACKING & BUDGETING
• Real-time monthly expense pacing with interactive budget progress bars.
• Instant average spend per receipt calculation.
• 6-month historical spending trends with visual comparison charts.
• Category breakdown showing your top spending areas (Groceries, Dining, Transport, Utilities, Health, and more).

🔍 POWERFUL LIBRARY & QUICK SEARCH
• Full-text search to find receipts by merchant or item name in milliseconds.
• One-tap category filters and custom tag filters.
• Tap to inspect the original receipt with smooth multi-touch pinch-to-zoom (up to 5×) and pan gestures.
• Edit merchant names, dates, categories, or totals whenever needed.

🔒 100% PRIVATE, SECURE & OFFLINE-FIRST
• Biometric App Lock: Protect your private expenses with your fingerprint, face unlock or screen lock.
• Zero cloud uploads: All data is saved inside a local SQLite database on your device.
• Zero tracking or analytics SDKs: No advertising trackers, no telemetry profiling your financial habits.
• No account or login required: Install the app and start scanning immediately.
• Zero ads: Enjoy an uninterrupted, clean, tactile financial workflow.

⚙️ CUSTOMIZABLE TO YOUR LIFE
• Create and customize your own expense categories with unique colors.
• Multi-currency support: USD ($), EUR (€), GBP (£), JPY (¥), CAD, AUD, AED, INR, and more.
• Flexible date formatting: YYYY-MM-DD, DD/MM/YYYY, or MM/DD/YYYY.
• PDF Expense Reports & CSV/JSON Export: Generate clean, itemized PDF reports for reimbursements or export spreadsheets for tax preparation.
• Multi-language support: English, German, Spanish, French, Italian, Dutch, and Portuguese.

Download Chit today and experience receipt tracking the way it was meant to be: fast, private, and effortless.
```

---

## 2. Categorization, Tags & Contact Details

- **Application Type:** App
- **Primary Category:** Finance
- **Secondary Category:** Productivity
- **Tags:**
  - Expense Tracker
  - Receipt Scanner
  - Personal Finance
  - Budget & Expense
  - OCR Scanner
- **Target Audience:** Ages 18 and older (General Audience)
- **Contains Ads:** **No** (Mark "No" in Play Console)
- **App Access:** All functionality is available without special access or credentials (no login required).

---

## 3. Google Play Data Safety Form Answers

Google Play requires all developers to complete the Data Safety questionnaire. Because Chit is strictly **offline-first with local SQLite storage**, your answers are straightforward:

### Overview Questions:
1. **Does your app collect or share any user data?**
   - **Answer: NO**
   - *Reason:* All receipt captures, line items, names, and budget numbers are stored strictly on the local device file system and local SQLite database (`expo-sqlite`). No external server synchronization exists.

2. **Is all user data encrypted in transit?**
   - **Answer: Not Applicable** (Zero data is transmitted).

3. **Can users request that their data be deleted?**
   - **Answer: YES**
   - *Reason:* Users can delete any individual receipt or reset all data at any time directly in the app settings.

### Permissions Declaration:
| Permission | Declared In Manifest | Justification for Google Play Review |
|:---|:---:|:---|
| `android.permission.CAMERA` | Yes | Required strictly for optical receipt scanning and capturing document photos for expense records. Photos remain on-device. |
| `android.permission.VIBRATE` | Yes | Provides tactile haptic feedback during UI interactions and successful scans. |
| `android.permission.READ_EXTERNAL_STORAGE` | Yes (`maxSdkVersion=32`) | Scoped storage access compliant with Android 13+ guidelines for photo picker. |
| `android.permission.WRITE_EXTERNAL_STORAGE` | Yes (`maxSdkVersion=32`) | Scoped storage access compliant with Android 13+ guidelines. |
| `android.permission.INTERNET` | Yes | Declared by standard React Native runtime; no user receipt or financial data is ever transmitted. |

---

## 4. Content Rating Questionnaire Answers

When filling out the IARC Content Rating questionnaire in Google Play Console:
- **Category:** Utility, Productivity, Communication, or Other
- **Violence:** No
- **Sexuality / Nudity:** No
- **Language / Profanity:** No
- **Controlled Substances:** No
- **Gambling:** No
- **User-to-User Interaction / Chat:** No
- **Shares User Location:** No
- **Allows users to purchase digital goods:** No
- **Resulting Rating:** **PEGI 3 / ESRB Everyone / USK 0** (Suitable for all audiences).

---

## 5. Visual Marketing Assets Summary

All required Google Play visual assets have been compiled and generated into `play-store/graphics/`:

| Asset Type | File Name | Dimensions | Specs |
|:---|:---|:---:|:---|
| **App Icon** | `icon-512x512.png` | 512 x 512 px | 32-bit PNG, no alpha, under 1024 KB |
| **Feature Graphic** | `feature-graphic-1024x500.png` | 1024 x 500 px | PNG, 2.048:1 aspect ratio, no transparency |
| **Phone Slide 1** | `slide-1-scanner.png` | 1080 x 2160 px | Smart On-Device OCR Scanner |
| **Phone Slide 2** | `slide-2-dashboard.png` | 1080 x 2160 px | Monthly Budgeting & Spending Trends |
| **Phone Slide 3** | `slide-3-extraction.png` | 1080 x 2160 px | Automated Merchant & Item Extraction |
| **Phone Slide 4** | `slide-4-library.png` | 1080 x 2160 px | Fast Receipts Library & Category Filters |
| **Phone Slide 5** | `slide-5-document.png` | 1080 x 2160 px | High-Res Document Viewer & Full Zoom |
| **Phone Slide 6** | `slide-6-privacy.png` | 1080 x 2160 px | 100% Private, Zero Cloud & Offline SQLite |

---

## 6. How to Upload to Google Play Console (Step-by-Step)

1. **Log in to Google Play Console**:
   - Go to [play.google.com/console](https://play.google.com/console).
   - Click **Create app**.
   - App name: `Chit: Receipt Scanner & OCR`
   - Default language: `English (United States)`
   - App or game: `App`
   - Free or paid: `Free`
   - Accept Declarations and click **Create app**.

2. **Upload Store Listing Assets**:
   - Navigate to **Grow** > **Store presence** > **Main store listing**.
   - Copy & paste the **Short description** and **Full description** from Section 1 above.
   - Upload `play-store/graphics/icon-512x512.png` to **App icon**.
   - Upload `play-store/graphics/feature-graphic-1024x500.png` to **Feature graphic**.
   - Upload `slide-1-scanner.png` through `slide-6-privacy.png` to **Phone screenshots**.

3. **Complete App Content Questionnaire**:
   - Navigate to **Policy and programs** > **App content**.
   - **Privacy Policy**: Enter the URL of your hosted `privacy.html` landing page.
   - **Ads**: Select "No, my app does not contain ads".
   - **App access**: Select "All functionality is available without special access".
   - **Content ratings**: Fill out questionnaire using answers from Section 4.
   - **Target audience**: Select "18 and older".
   - **Data safety**: Fill out questionnaire using answers from Section 3.

4. **Upload Production Release Bundle**:
   - Navigate to **Release** > **Production**.
   - Click **Create new release**.
   - Upload: `android/app/build/outputs/bundle/release/app-release.aab`.
   - Release name: `1.0.0 (1)`.
   - Release notes:
     ```text
     Initial production release of Chit - Receipt Scanner & Expense Tracker.
     - On-device optical character recognition (OCR) for instant receipt capture.
     - Monthly budgeting and spending analytics.
     - Categorization, merchant search, and high-res document viewer.
     - 100% private, offline SQLite storage.
     ```
   - Click **Next**, review the release checks, and click **Start rollout to Production**!
