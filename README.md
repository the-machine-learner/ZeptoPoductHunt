# ⚡ Zepto Product Hunt Week MVP

> A gamified, high-converting engagement campaign prototype built for **Zepto Quick Commerce** to boost DAUs, category exploration, and average order value (AOV) via progressive AI riddle clues and flash rewards.

---

## 🌟 Features & Highlights

- **🎯 Gamified Progressive Clue Hunt**
  - **Clue 1 & Clue 2**: Past unlocked clues guiding users across categories.
  - **Clue 3 Active Challenge**: Spicy AI riddle challenge (*"I test friendships, press your buttons... next to your TV."*).
- **🛍️ Mystery Product Discovery (No Spoilers)**
  - Catalog and PDP screens display **regular undiscounted prices** with zero explicit spoiler tags.
  - Users independently deduce secret items via clues.
- **🔐 Dynamic Reward & Coupon Unlocking**
  - **Locked State**: Adding regular non-hunt items keeps the coupon `ACCZ50OFF` **🔒 LOCKED**.
  - **Unlocked State**: Adding the secret Hunt item (**Zebronics MAX FURY RGB Gamepad**) completes Clue 3, unlocking:
    - **Discovered Deal**: ₹1,999 ➔ ₹1,080 (-₹919)
    - **Coupon `ACCZ50OFF`**: Extra -₹50 OFF
    - **Final Payment**: **₹1,030** with celebratory confetti! 🎉
- **📱 Pixel-Perfect Mobile UI Overlay**
  - Built inside a responsive mobile frame fitting standard laptop viewports.
  - Centered floating **Modal Overlay Card** matching production Zepto design mockups.
  - Dedicated tabs for **Walkthrough Carousel**, **My Clues**, and **My Rewards**.
- **🚀 11-Step Interactive Guided Tour**
  - Controlled via Streamlit sidebar controls (`▶ Start Tour`, `🔄 Reset Demo`).
  - Transparent backdrop cutout mask allowing direct interactive clicks.
  - Teaches users how adding a non-hunt item keeps the coupon locked vs. adding the secret hunt item unlocking the prize.

---

## 🛠️ Tech Stack

- **Frontend Frame**: [Streamlit](https://streamlit.io/) (Python)
- **UI Application**: React 18 (Babel JSX in-browser transpilation)
- **Styling**: Modern CSS3 (Glassmorphism, Tailwind utilities, dynamic overlays)
- **Effects**: `canvas-confetti` for celebratory reward unlocks
- **Icons**: Lucide Icons & Custom SVG UI graphics

---

## 🚀 Quick Start (Run Locally)

### 1. Clone & Navigate
```bash
cd ZeptoPoductHunt
```

### 2. Create & Activate Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install streamlit
```

### 4. Run App
```bash
streamlit run streamlit_app.py
```

Open your browser at **`http://localhost:8501`** to experience the MVP!

---

## 🕹️ Demo Mode Controls

In the Streamlit left sidebar:
- **`▶ Start Tour`**: Launches the 11-step guided overlay tour demonstrating the end-to-end user journey.
- **`🔄 Reset Demo`**: Resets app state, cart items, and tutorial progress back to initial state.

---

## 📄 License
This project is created for product management demonstration & prototype validation purposes.
