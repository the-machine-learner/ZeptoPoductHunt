# ⚡ Zepto Product Hunt Week – AI-Enabled MVP

> A gamified, high-converting engagement campaign MVP built for **Zepto Quick Commerce** powered by **Groq LLM (Llama 3.3 70B)** to dynamically generate personalized riddle clues, boost DAUs, encourage multi-category exploration, and lift average order value (AOV).

---

## 🌟 Key Features & Entry Flows

### 🚪 1. Two Product Hunt Entry Flows

- **Flow 1 – Guided Tutorial (Default Demo Profile)**
  - Designed for first-time users, demos, and judges.
  - Automatically selects default persona **Arjun Patel (Gaming & Tech Enthusiast)**.
  - Triggers the Shared Backend Initialization Pipeline & Groq AI Clue generation.
  - Launches an interactive 11-step guided walkthroughoverlay directly inside the mobile frame.

- **Flow 2 – Profile Selection (Persona Explorer)**
  - Designed for exploring different customer personas:
    1. 🎮 **Arjun Patel** (*Gaming & Tech Enthusiast*)
    2. 💄 **Ananya Sharma** (*Beauty & Skincare Lover*)
    3. 🍕 **Rohan Verma** (*Late-Night Munchie Monster*)
    4. 🧺 **Priya & Vikram** (*Household & Family Replenishers*)
  - Each persona features its own purchase history, tone preference, unexplored target categories, and personalized catalog.

---

### 🧠 2. Shared Backend Initialization & Groq AI Pipeline

Both entry flows invoke the same backend initialization pipeline:
1. Loads selected customer profile.
2. Reads user's purchase history & explored categories.
3. Identifies eligible unexplored categories.
4. Selects target secret product.
5. Invokes **Groq API (`llama-3.3-70b-versatile`)** to generate a personalized riddle clue.
6. Populates personalized catalog & returns complete session data to the frontend.

---

### 🔄 3. Continuous AI Gameplay Loop & Progressive Simplification

The hunt is dynamic rather than static:
- **Initialization** generates Clue 1.
- **Completed Purchases** trigger subsequent AI generation cycles for Clue 2 and Clue 3.
- **Progressive Difficulty Rule**:
  - **Clue 1 (Clever Riddle)**: Witty, non-obvious riddle reflecting user persona & purchase history.
  - **Clue 2 (Simpler Hint)**: Gives category & usage benefit hints.
  - **Clue 3 (Direct Actionable Clue)**: Explicitly guides the user to the target product so they can finish the hunt easily!

---

### 🔐 4. Dynamic Reward & Coupon Unlocking

- **Locked State**: Adding regular non-hunt items keeps coupon `ACCZ50OFF` **🔒 LOCKED**.
- **Unlocked State**: Adding the secret hunt item completes the challenge, unlocking:
  - **Discovered Deal**: ₹1,999 ➔ ₹1,080
  - **Coupon `ACCZ50OFF`**: Extra -₹50 OFF
  - **Final Payment**: **₹1,030** with celebratory confetti! 🎉

---

## 🛠️ Tech Stack & API Configuration

- **Frontend Frame**: [Streamlit](https://streamlit.io/) (Python)
- **UI Application**: React 18 (Babel JSX in-browser transpilation)
- **AI Engine**: [Groq API](https://groq.com/) using `llama-3.3-70b-versatile` (JSON mode)
- **Secrets Management**: Streamlit Secrets (`st.secrets["GROQ_API_KEY"]` / `.streamlit/secrets.toml`)
- **Effects**: `canvas-confetti` for celebratory unlocks

---

## 🚀 Quick Start (Run Locally)

### 1. Clone & Navigate
```bash
cd ZeptoPoductHunt
```

### 2. Configure Streamlit Secrets (`.streamlit/secrets.toml`)
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

### 3. Install & Run App
```bash
pip install streamlit requests
streamlit run streamlit_app.py
```

Visit `http://localhost:8501` to test the AI-Enabled Product Hunt MVP!
