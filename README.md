# AtCoder Aesthetic Dark Mode Chrome Extension

A beautiful, premium, handcrafted dark theme for the AtCoder website (`https://atcoder.jp/*`). Built as a lightweight Manifest V3 Chrome extension, this theme avoids raw color inversion (which corrupts syntax highlighting and rating badges) and instead targets specific layouts individually.

---

## Key Features

1. **Strictly Handcrafted (No Filters):** Semantic statuses like **Accepted (AC)**, **Wrong Answer (WA)**, and **Waiting for Judgment (WJ)** are individually mapped to beautiful dark-mode equivalent backgrounds.
2. **Preventing "White Flash":** The theme state is read and applied on `document_start` directly onto the `<html>` root, ensuring no white screen flash during page loading.
3. **Readable Ratings:** User handles retain their original colors (Gray, Brown, Green, Cyan, Blue, Yellow, Orange, Red) but are adjusted for high legibility on a dark background.
4. **Code Editors Darkened:** Code editor containers for both CodeMirror and Ace Editor are fully styled with custom syntax highlighting schemes.
5. **Dynamic Live Syncing:** Toggling the state from the extension popup instantly swaps the theme on all open AtCoder tabs without reloading the pages.

---

## File Structure

```
c:\SamStuff\Atcoder-web-extension\
├── manifest.json       # Extension manifest (MV3)
├── content.js          # Handles page load theme rendering and runtime toggles
├── theme.css           # Custom dark mode stylesheet (overrides Bootstrap 3 elements)
├── popup.html          # Pop-up panel interface
├── popup.js            # Syncs state between toggle switch and storage
├── generate_icons.py   # Python helper using PIL to build icons
└── icons/              # Generated extension PNG icons (16x16, 48x48, 128x128)
```

---

## How to Install and Test

### 1. Load the Extension into Google Chrome
1. Open Google Chrome.
2. Navigate to: `chrome://extensions/`
3. Toggle on **Developer mode** in the upper-right corner.
4. Click the **Load unpacked** button in the upper-left corner.
5. Select the extension directory: `c:\SamStuff\Atcoder-web-extension`

### 2. Verify Functionality
1. Go to [AtCoder Home](https://atcoder.jp/).
2. Click the extension puzzle icon in the Chrome toolbar and pin **AtCoder Aesthetic Dark Mode**.
3. Click the extension icon. You will see a beautifulOutfit-themed glassmorphism card with a toggle switch.
4. Try toggling **Dark Mode** on/off. Notice how AtCoder changes theme instantly!
5. Navigate through the task lists, submission badges, standings tables, code editors, and user profiles to inspect the handcrafted styling.
