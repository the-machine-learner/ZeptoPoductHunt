import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Zepto Product Hunt - Gamified Discovery MVP",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Streamlit Shell
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1.5rem;
        max-width: 1200px;
    }
    stApp {
        background-color: #0f172a;
    }
</style>
""", unsafe_allow_html=1)

# Sidebar Information & Controls
st.sidebar.title("🎯 Zepto Product Hunt")
st.sidebar.markdown("**Gamified Category Discovery Engine MVP**")

st.sidebar.info("""
**Interactive Flow Demo:**
1. **Screen 1 (Home)**: Tap the **Hunt** nav item at bottom right.
2. **Screen 2 (Walkthrough)**: View 4-step game rules.
3. **Screen 3 (Clue Challenge)**: Read Level 3 riddle (*"I test friendships, press your buttons..."*).
4. **Screen 4 (Rewards)**: Check Prize ₹50 OFF.
5. **Screen 6 (Category)**: Navigate to Electronics & Gaming.
6. **Screen 7 (PDP)**: Open Zebronics MAX FURY RGB Gamepad & tap **Add to Cart**.
7. **Screen 8 (Cart)**: View unlocked Coupon Code `ACCZ50OFF` + Celebration Banner!
""")

st.sidebar.markdown("---")
st.sidebar.caption("Built for Product Management Showcase • Gen Z Discovery Engine")

# Build Standalone Single-File HTML with React Bundle
html_content = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Zepto Product Hunt - Mobile MVP</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- React & ReactDOM CDN -->
    <script src="https://unpkg.com/react@18/umd/react.production.min.js" crossorigin></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js" crossorigin></script>
    <!-- Babel standalone for JSX -->
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <!-- Canvas Confetti -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>

    <style>
      :root {
        --zepto-green: #0c831f;
        --zepto-green-light: #10b981;
        --zepto-green-bg: #e6f4ea;
        --zepto-pink: #ff3269;
        --zepto-purple: #6366f1;
        --zepto-dark: #0f172a;
        --zepto-gray-100: #f8fafc;
        --zepto-gray-200: #f1f5f9;
        --zepto-gray-300: #e2e8f0;
        --zepto-gray-800: #1e293b;
        --font-main: 'Inter', sans-serif;
        --font-display: 'Outfit', sans-serif;
      }
      * { box-sizing: border-box; margin: 0; padding: 0; }
      body {
        font-family: var(--font-main);
        background-color: #0f172a;
        color: var(--zepto-gray-800);
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        padding: 10px;
      }
      .app-viewport-container {
        width: 100%;
        max-width: 480px;
        display: flex;
        flex-direction: column;
        align-items: center;
      }
      .control-header {
        width: 100%;
        background: rgba(30, 41, 59, 0.85);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 10px 16px;
        margin-bottom: 14px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
      }
      .btn-tour-restart {
        background: linear-gradient(135deg, var(--zepto-pink), #ec4899);
        color: white;
        border: none;
        padding: 8px 14px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.8rem;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(255, 50, 105, 0.4);
      }
      .mobile-device-frame {
        width: 380px;
        height: 800px;
        background: #ffffff;
        border-radius: 40px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6), 0 0 0 10px #1e293b;
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
      }
      .status-bar {
        height: 40px;
        background: #0c831f;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 20px;
        font-size: 0.8rem;
        font-weight: 600;
        z-index: 40;
      }
      .phone-notch {
        position: absolute;
        top: 6px;
        left: 50%;
        transform: translateX(-50%);
        width: 110px;
        height: 24px;
        background: #000000;
        border-radius: 16px;
        z-index: 50;
      }
      .mobile-screen-body {
        flex: 1;
        overflow-y: auto;
        position: relative;
        background-color: var(--zepto-gray-100);
        display: flex;
        flex-direction: column;
      }
      .bottom-nav-bar {
        height: 60px;
        background: #ffffff;
        border-top: 1px solid var(--zepto-gray-300);
        display: flex;
        justify-content: space-around;
        align-items: center;
        z-index: 30;
      }
      .nav-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 2px;
        color: #64748b;
        font-size: 0.65rem;
        font-weight: 600;
        cursor: pointer;
        position: relative;
      }
      .nav-item.active { color: var(--zepto-green); }
      .nav-item.hunt-highlight { color: var(--zepto-pink); font-weight: 800; }
      .hunt-badge {
        position: absolute;
        top: -6px;
        right: -4px;
        background: var(--zepto-pink);
        color: white;
        font-size: 0.55rem;
        padding: 1px 5px;
        border-radius: 10px;
        font-weight: 900;
        box-shadow: 0 2px 6px rgba(255, 50, 105, 0.4);
      }
      .home-header {
        background: linear-gradient(180deg, #0c831f 0%, #10b981 100%);
        color: white;
        padding: 12px 14px 14px 14px;
        border-bottom-left-radius: 18px;
        border-bottom-right-radius: 18px;
      }
      .location-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
      .eta-pill { background: rgba(255, 255, 255, 0.25); padding: 4px 8px; border-radius: 16px; font-size: 0.75rem; font-weight: 800; }
      .search-box-wrap { position: relative; margin-bottom: 10px; }
      .search-input {
        width: 100%;
        background: white;
        border: none;
        border-radius: 12px;
        padding: 10px 12px 10px 36px;
        font-size: 0.8rem;
        color: var(--zepto-gray-800);
      }
      .pet-store-chip {
        position: absolute;
        right: 6px;
        top: 50%;
        transform: translateY(-50%);
        background: #fef3c7;
        color: #d97706;
        font-size: 0.65rem;
        font-weight: 700;
        padding: 3px 6px;
        border-radius: 8px;
      }
      .category-chips-scroll { display: flex; gap: 6px; overflow-x: auto; padding-bottom: 2px; }
      .cat-chip {
        background: rgba(255, 255, 255, 0.2);
        color: white;
        padding: 4px 10px;
        border-radius: 16px;
        font-size: 0.72rem;
        font-weight: 600;
        white-space: nowrap;
        cursor: pointer;
      }
      .cat-chip.active { background: white; color: var(--zepto-green); font-weight: 700; }
      .cat-chip.highlight-box { border: 2px solid var(--zepto-pink); }

      .home-content-body { padding: 12px; display: flex; flex-direction: column; gap: 12px; }
      .floating-hunt-banner {
        background: linear-gradient(135deg, var(--zepto-pink), #ec4899);
        color: white;
        padding: 10px 14px;
        border-radius: 14px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        cursor: pointer;
        box-shadow: 0 4px 16px rgba(255, 50, 105, 0.4);
      }
      .category-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
      .cat-card {
        background: white;
        border-radius: 12px;
        padding: 8px 6px;
        text-align: center;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
        cursor: pointer;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 4px;
      }
      .cat-card-img { width: 38px; height: 38px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; }
      .cat-card-title { font-size: 0.68rem; font-weight: 700; color: var(--zepto-gray-800); }
      .cat-card-off { font-size: 0.6rem; font-weight: 800; color: var(--zepto-green); background: var(--zepto-green-bg); padding: 2px 4px; border-radius: 4px; }
      .steal-deals-banner {
        background: linear-gradient(135deg, #1e1b4b, #312e81);
        color: white;
        border-radius: 14px;
        padding: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }

      /* Modal Bottom Sheet */
      .modal-overlay {
        position: absolute; inset: 0; background: rgba(0, 0, 0, 0.65); backdrop-filter: blur(4px); z-index: 100; display: flex; flex-direction: column; justify-content: flex-end;
      }
      .modal-bottom-sheet {
        background: #ffffff; border-top-left-radius: 24px; border-top-right-radius: 24px; padding: 18px 18px 20px 18px; max-height: 90%; overflow-y: auto; position: relative;
      }
      .modal-close-btn {
        position: absolute; top: 14px; right: 14px; background: var(--zepto-gray-200); width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; color: #64748b; font-weight: 700;
      }
      .modal-header-title { text-align: center; font-family: var(--font-display); font-weight: 800; font-size: 1.15rem; color: var(--zepto-green); margin-bottom: 12px; }
      
      .step-card { background: var(--zepto-gray-100); border-radius: 12px; padding: 10px 12px; margin-bottom: 8px; display: flex; gap: 10px; align-items: flex-start; }
      .step-icon-wrap { width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1rem; flex-shrink: 0; }
      .step-icon-1 { background: #dcfce7; color: #15803d; }
      .step-icon-2 { background: #f3e8ff; color: #7e22ce; }
      .step-icon-3 { background: #fee2e2; color: #b91c1c; }
      .step-icon-4 { background: #dbeafe; color: #1d4ed8; }

      .modal-nav-bar { display: flex; justify-content: space-around; background: var(--zepto-gray-100); border-radius: 16px; padding: 4px; margin-top: 14px; }
      .modal-nav-tab { flex: 1; text-align: center; padding: 6px 0; border-radius: 12px; font-size: 0.72rem; font-weight: 700; color: #64748b; cursor: pointer; }
      .modal-nav-tab.active { background: white; color: var(--zepto-green); box-shadow: 0 2px 6px rgba(0,0,0,0.08); }

      .level-progress-bar { display: flex; justify-content: center; gap: 10px; margin-bottom: 12px; }
      .level-badge { width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; font-weight: 700; background: var(--zepto-gray-200); color: #64748b; }
      .level-badge.done { background: var(--zepto-green); color: white; }
      .level-badge.current { border: 2px solid var(--zepto-green); color: var(--zepto-green); }

      .clue-box { background: #f0fdf4; border: 1.5px dashed #22c55e; border-radius: 16px; padding: 14px; text-align: center; margin-bottom: 12px; }
      .clue-riddle { font-size: 0.82rem; font-weight: 600; color: var(--zepto-gray-800); line-height: 1.4; font-style: italic; margin-bottom: 10px; }
      .hint-pill-btn { background: var(--zepto-green); color: white; border: none; padding: 6px 12px; border-radius: 16px; font-size: 0.72rem; font-weight: 700; cursor: pointer; }

      .reward-card-purple { background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; border-radius: 18px; padding: 20px; text-align: center; }
      .unlock-now-btn { background: white; color: #4f46e5; border: none; width: 100%; padding: 10px; border-radius: 12px; font-size: 0.85rem; font-weight: 800; margin-top: 10px; cursor: pointer; }

      /* PDP & Cart */
      .pdp-image-box { background: white; padding: 20px; display: flex; justify-content: center; position: relative; }
      .rating-badge { position: absolute; bottom: 10px; left: 14px; background: #f1f5f9; padding: 3px 6px; border-radius: 6px; font-size: 0.7rem; font-weight: 800; }
      .pdp-info-card { background: white; padding: 14px; margin-top: 6px; }
      .pdp-title { font-size: 0.85rem; font-weight: 700; line-height: 1.3; color: var(--zepto-gray-800); margin-bottom: 6px; }
      .sticky-bottom-add { position: absolute; bottom: 0; left: 0; right: 0; background: white; padding: 10px 14px; border-top: 1px solid var(--zepto-gray-200); display: flex; gap: 10px; align-items: center; z-index: 30; }
      .btn-add-cart-pink { flex: 1; background: var(--zepto-pink); color: white; border: none; padding: 12px; border-radius: 12px; font-size: 0.88rem; font-weight: 800; cursor: pointer; }

      .cart-hunt-card { background: #f0fdf4; border: 1.5px solid #22c55e; border-radius: 16px; padding: 12px; margin: 12px 0; text-align: center; }
      .coupon-code-badge { background: #22c55e; color: white; padding: 4px 12px; border-radius: 8px; font-weight: 900; font-size: 0.78rem; display: inline-block; margin: 6px 0; }

      /* GUIDED TUTORIAL OVERLAY */
      .tutorial-overlay-mask { position: absolute; inset: 0; background: rgba(15, 23, 42, 0.8); z-index: 200; }
      .tutorial-tooltip-card {
        position: absolute; background: white; border-radius: 16px; padding: 14px; width: calc(100% - 24px); left: 12px; box-shadow: 0 12px 30px rgba(0,0,0,0.35); z-index: 220; border: 2px solid var(--zepto-green);
      }
      .tutorial-step-badge { background: var(--zepto-green-bg); color: var(--zepto-green); font-size: 0.65rem; font-weight: 900; padding: 2px 6px; border-radius: 8px; display: inline-block; margin-bottom: 4px; }
      .tutorial-title { font-family: var(--font-display); font-size: 0.92rem; font-weight: 800; color: var(--zepto-gray-800); margin-bottom: 2px; }
      .tutorial-desc { font-size: 0.72rem; color: #475569; line-height: 1.35; margin-bottom: 10px; }
      .tutorial-btn-row { display: flex; justify-content: space-between; align-items: center; }
      .btn-tut-skip { background: none; border: none; color: #94a3b8; font-size: 0.7rem; font-weight: 700; cursor: pointer; }
      .btn-tut-next { background: var(--zepto-green); color: white; border: none; padding: 6px 14px; border-radius: 10px; font-size: 0.75rem; font-weight: 800; cursor: pointer; }
      .highlight-cutout {
        position: absolute; border-radius: 14px; border: 3px solid var(--zepto-pink); box-shadow: 0 0 0 9999px rgba(15, 23, 42, 0.8), 0 0 16px rgba(255, 50, 105, 0.9); z-index: 210; pointer-events: none;
      }
    </style>
  </head>
  <body>
    <div id="root"></div>

    <script type="text/babel">
      const { useState, useEffect } = React;

      function App() {
        const [screen, setScreen] = useState('home');
        const [showModal, setShowModal] = useState(false);
        const [modalTab, setModalTab] = useState('walkthrough');
        const [cartCount, setCartCount] = useState(0);
        const [tutorialStep, setTutorialStep] = useState(1);
        const [targetRect, setTargetRect] = useState(null);

        useEffect(() => {
          if (tutorialStep <= 0) { setTargetRect(null); return; }
          const updateRect = () => {
            let targetId = '';
            if (tutorialStep === 1) targetId = 'nav-hunt-btn';
            else if (tutorialStep === 2) targetId = 'modal-tab-walkthrough';
            else if (tutorialStep === 3) targetId = 'modal-tab-clues';
            else if (tutorialStep === 4) targetId = 'modal-tab-rewards';
            else if (tutorialStep === 5) targetId = 'cat-chip-electronics';
            else if (tutorialStep === 6) targetId = 'product-card-gamepad';
            else if (tutorialStep === 7) targetId = 'btn-add-to-cart-pdp';
            else if (tutorialStep === 8) targetId = 'cart-hunt-card-target';

            const el = document.getElementById(targetId);
            if (el) {
              const rect = el.getBoundingClientRect();
              setTargetRect({ top: rect.top, left: rect.left, width: rect.width, height: rect.height });
            } else { setTargetRect(null); }
          };
          const timer = setTimeout(updateRect, 300);
          return () => clearTimeout(timer);
        }, [tutorialStep, screen, showModal, modalTab]);

        const triggerConfetti = () => {
          if (window.confetti) window.confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
        };

        const getTutorialStepData = () => {
          switch (tutorialStep) {
            case 1: return { title: "Step 1: Open Product Hunt", description: "Tap the highlighted 'Hunt' icon at the bottom right to enter Product Hunt Week!", buttonText: "Open Hunt →", tooltipBottom: 75, onAction: () => { setShowModal(true); setModalTab('walkthrough'); setTutorialStep(2); } };
            case 2: return { title: "Step 2: Walkthrough (How It Works)", description: "Review 4-step game rules: Buy Products → Unlock Clues → Find Item → Get Discount!", buttonText: "View Clue →", tooltipBottom: 140, onAction: () => { setModalTab('clues'); setTutorialStep(3); } };
            case 3: return { title: "Step 3: Read Spicy AI Clue", description: "Level 3 Challenge: 'I test friendships, press your buttons... next to your TV.' Hint: Gaming!", buttonText: "Check Rewards →", tooltipBottom: 140, onAction: () => { setModalTab('rewards'); setTutorialStep(4); } };
            case 4: return { title: "Step 4: Check Prize", description: "Prize: ₹50 OFF Coupon code for your cart when you find & add the secret item!", buttonText: "Go Hunt Item →", tooltipBottom: 140, onAction: () => { setShowModal(false); setScreen('category'); setTutorialStep(6); } };
            case 5: return { title: "Step 5: Browse Category", description: "Navigate to Electronics & Gaming where the clue item is located.", buttonText: "Go to Gaming →", tooltipTop: 140, onAction: () => { setScreen('category'); setTutorialStep(6); } };
            case 6: return { title: "Step 6: Select Secret Product", description: "Found it! Tap on the Zebronics MAX FURY RGB Gamepad (Hunt Item Detected).", buttonText: "Open Item →", tooltipBottom: 75, onAction: () => { setScreen('pdp'); setTutorialStep(7); } };
            case 7: return { title: "Step 7: Add to Cart", description: "Tap 'Add to Cart' to trigger the Flash Sale price and unlock your coupon code!", buttonText: "Add to Cart →", tooltipBottom: 75, onAction: () => { setCartCount(1); setScreen('cart'); setTutorialStep(8); triggerConfetti(); } };
            case 8: return { title: "Step 8: Coupon ACCZ50OFF Unlocked! 🎉", description: "Boom! Level 3 complete. COUPON CODE: ACCZ50OFF is unlocked & applied to your cart!", buttonText: "Finish Tour 🚀", tooltipTop: 90, onAction: () => { setTutorialStep(0); } };
            default: return null;
          }
        };

        const currentStepData = getTutorialStepData();

        const handleRestart = () => {
          setScreen('home'); setShowModal(false); setModalTab('walkthrough'); setCartCount(0); setTutorialStep(1);
        };

        return (
          <div className="app-viewport-container">
            <header className="control-header">
              <div style={{ fontWeight: 800, fontSize: '1rem' }}>Zepto Product Hunt MVP</div>
              <button className="btn-tour-restart" onClick={handleRestart}>▶ Restart Tour</button>
            </header>

            <div className="mobile-device-frame">
              <div className="status-bar">
                <div>11:08</div>
                <div className="phone-notch"></div>
                <div>5G ⚡6m 🔋</div>
              </div>

              <div className="mobile-screen-body">
                {screen === 'home' && (
                  <div style={{ display: 'flex', flexDirection: 'column', flex: 1 }}>
                    <div className="home-header">
                      <div className="location-bar">
                        <div>
                          <div style={{ fontSize: '0.6rem', opacity: 0.8, fontWeight: 700 }}>DELIVERING TO</div>
                          <div style={{ fontSize: '0.75rem', fontWeight: 700 }}>Flat - 803, Ruby, Gulmohar Orch...</div>
                        </div>
                        <div className="eta-pill">⚡ 6 minutes</div>
                      </div>

                      <div className="search-box-wrap">
                        <input className="search-input" placeholder='Search for "Face Wash"' readOnly onClick={() => { setScreen('category'); setTutorialStep(6); }} />
                        <div className="pet-store-chip">🐶 Pet Store</div>
                      </div>

                      <div className="category-chips-scroll">
                        <div className="cat-chip active">All</div>
                        <div className="cat-chip">Fresh</div>
                        <div id="cat-chip-electronics" className={`cat-chip ${tutorialStep === 5 ? 'highlight-box' : ''}`} onClick={() => { setScreen('category'); setTutorialStep(6); }}>⚡ Electronics</div>
                        <div className="cat-chip">Fashion</div>
                      </div>
                    </div>

                    <div className="home-content-body">
                      <div className="floating-hunt-banner" onClick={() => { setShowModal(true); setModalTab('walkthrough'); if(tutorialStep===1) setTutorialStep(2); }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <span style={{ fontSize: '1.4rem' }}>🎯</span>
                          <div>
                            <div style={{ fontSize: '0.68rem', fontWeight: 800, opacity: 0.9 }}>LIMITED TIME EVENT</div>
                            <div style={{ fontSize: '0.9rem', fontWeight: 900 }}>PRODUCT HUNT WEEK</div>
                          </div>
                        </div>
                        <button style={{ background: 'white', color: '#ff3269', border: 'none', padding: '4px 10px', borderRadius: '14px', fontWeight: 800, fontSize: '0.72rem' }}>PLAY NOW →</button>
                      </div>

                      <div style={{ fontSize: '0.8rem', fontWeight: 800, color: '#334155' }}>Explore Categories</div>
                      <div className="category-grid">
                        <div className="cat-card"><div className="cat-card-img" style={{ background: '#fef3c7' }}>🥦</div><div className="cat-card-title">Essentials</div><div className="cat-card-off">70% OFF</div></div>
                        <div className="cat-card"><div className="cat-card-img" style={{ background: '#fce7f3' }}>🧴</div><div className="cat-card-title">Personal</div><div className="cat-card-off">85% OFF</div></div>
                        <div className="cat-card" onClick={() => { setScreen('category'); setTutorialStep(6); }}><div className="cat-card-img" style={{ background: '#e0e7ff' }}>🎮</div><div className="cat-card-title">Gaming</div><div className="cat-card-off" style={{ background: '#e0e7ff', color: '#4338ca' }}>HUNT ITEM</div></div>
                      </div>

                      <div className="steal-deals-banner">
                        <div>
                          <div style={{ fontSize: '0.68rem', color: '#fbbf24', fontWeight: 800 }}>OFFERS & DISCOUNTS</div>
                          <div style={{ fontSize: '0.88rem', fontWeight: 800 }}>Unlock extra ₹50 OFF</div>
                        </div>
                        <div style={{ background: '#ff3269', color: 'white', width: '32px', height: '32px', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 900 }}>%</div>
                      </div>
                    </div>

                    <div className="bottom-nav-bar">
                      <div className="nav-item active"><span>Home</span></div>
                      <div className="nav-item" onClick={() => setScreen('category')}><span>Categories</span></div>
                      <div className="nav-item"><span>Buy Again</span></div>
                      <div className="nav-item"><span>Print</span></div>
                      <div id="nav-hunt-btn" className="nav-item hunt-highlight" onClick={() => { setShowModal(true); setModalTab('walkthrough'); if(tutorialStep===1) setTutorialStep(2); }}>
                        <span className="hunt-badge">EVENT</span>
                        <span>🔥 Hunt</span>
                      </div>
                    </div>
                  </div>
                )}

                {screen === 'category' && (
                  <div style={{ display: 'flex', flexDirection: 'column', flex: 1, padding: '12px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '12px' }}>
                      <button onClick={() => setScreen('home')} style={{ border: 'none', background: 'none', fontSize: '1.2rem', cursor: 'pointer' }}>←</button>
                      <input className="search-input" value="Gaming & Electronics" readOnly style={{ background: '#e2e8f0' }} />
                    </div>

                    <div style={{ fontSize: '0.85rem', fontWeight: 900, marginBottom: '8px' }}>Trending deals</div>
                    <div id="product-card-gamepad" style={{ background: 'white', borderRadius: '16px', padding: '12px', display: 'flex', gap: '12px', border: tutorialStep===6 ? '2px solid #ff3269' : '1px solid #e2e8f0', cursor: 'pointer' }} onClick={() => { setScreen('pdp'); setTutorialStep(7); }}>
                      <div style={{ background: '#0f172a', borderRadius: '12px', padding: '8px', fontSize: '2rem' }}>🎮</div>
                      <div>
                        <div style={{ background: '#ffedd5', color: '#c2410c', fontSize: '0.6rem', fontWeight: 800, padding: '2px 4px', borderRadius: '4px', display: 'inline-block' }}>🎯 HUNT ITEM DETECTED</div>
                        <div style={{ fontSize: '0.8rem', fontWeight: 800, margin: '4px 0' }}>Zebronics MAX FURY RGB Gamepad</div>
                        <div style={{ fontSize: '0.9rem', fontWeight: 900 }}>₹1080 <span style={{ fontSize: '0.7rem', textDecoration: 'line-through', color: '#94a3b8' }}>₹1999</span></div>
                      </div>
                    </div>
                  </div>
                )}

                {screen === 'pdp' && (
                  <div style={{ display: 'flex', flexDirection: 'column', flex: 1, position: 'relative' }}>
                    <div style={{ padding: '10px 14px' }}>
                      <button onClick={() => setScreen('category')} style={{ border: 'none', background: 'none', fontSize: '1.2rem', cursor: 'pointer' }}>← Back</button>
                    </div>
                    <div className="pdp-image-box">
                      <div style={{ background: '#0f172a', borderRadius: '20px', padding: '24px', fontSize: '4rem' }}>🎮</div>
                      <div className="rating-badge">4.2 ★ 581</div>
                    </div>
                    <div className="pdp-info-card">
                      <div className="pdp-title">Zebronics MAX FURY Transparent RGB LED Wired Gamepad | Dual Motor Force Feedback</div>
                      <div style={{ fontSize: '1.1rem', fontWeight: 900, marginTop: '8px' }}>₹1080 <span style={{ fontSize: '0.75rem', textDecoration: 'line-through', color: '#94a3b8' }}>₹1999</span></div>
                    </div>
                    <div className="sticky-bottom-add">
                      <button id="btn-add-to-cart-pdp" className="btn-add-cart-pink" onClick={() => { setCartCount(1); setScreen('cart'); setTutorialStep(8); triggerConfetti(); }}>Add to Cart</button>
                    </div>
                  </div>
                )}

                {screen === 'cart' && (
                  <div style={{ display: 'flex', flexDirection: 'column', flex: 1, padding: '12px' }}>
                    <div style={{ fontSize: '0.85rem', fontWeight: 900, marginBottom: '4px' }}>Home Checkout</div>
                    <div style={{ background: '#e6f4ea', color: '#0c831f', fontSize: '0.75rem', fontWeight: 800, padding: '6px', borderRadius: '6px', textAlign: 'center', marginBottom: '10px' }}>Yay! You saved ₹959 on this order 🎉</div>

                    <div className="cart-hunt-card" id="cart-hunt-card-target">
                      <div className="level-progress-bar">
                        <div className="level-badge done">✓</div>
                        <div className="level-badge done">✓</div>
                        <div className="level-badge done" style={{ background: '#22c55e' }}>✓</div>
                      </div>
                      <div className="coupon-code-badge">COUPON CODE: ACCZ50OFF</div>
                      <div style={{ fontSize: '1rem', fontWeight: 900, color: '#15803d' }}>Congratulations !!! 🎉</div>
                      <div style={{ fontSize: '0.7rem', color: '#166534' }}>Level 3 Complete! You unlocked ₹50 OFF + Free Delivery on this order.</div>
                    </div>

                    <div className="sticky-bottom-add" style={{ flexDirection: 'column' }}>
                      <button className="btn-add-cart-pink" onClick={() => { alert('🎉 Order Placed Successfully!'); handleRestart(); }}>Pay ₹1080</button>
                    </div>
                  </div>
                )}

                {showModal && (
                  <div className="modal-overlay">
                    <div className="modal-bottom-sheet">
                      <div className="modal-close-btn" onClick={() => setShowModal(false)}>✕</div>
                      <div className="modal-header-title">PRODUCT HUNT WEEK</div>

                      {modalTab === 'walkthrough' && (
                        <div>
                          <div className="step-card"><div className="step-icon-wrap step-icon-1">🛍️</div><div><strong>STEP 1: Buy Products</strong><br/><span style={{fontSize:'0.7rem'}}>Select products with Hunt badge.</span></div></div>
                          <div className="step-card"><div className="step-icon-wrap step-icon-2">🗝️</div><div><strong>STEP 2: Unlock Clues</strong><br/><span style={{fontSize:'0.7rem'}}>Every purchase unlocks a clue.</span></div></div>
                          <div className="step-card"><div className="step-icon-wrap step-icon-3">🔍</div><div><strong>STEP 3: Find the Item</strong><br/><span style={{fontSize:'0.7rem'}}>Solve puzzle and locate secret item.</span></div></div>
                          <div className="step-card"><div className="step-icon-wrap step-icon-4">🏷️</div><div><strong>STEP 4: Get Discount</strong><br/><span style={{fontSize:'0.7rem'}}>Add item to cart & watch price drop!</span></div></div>
                        </div>
                      )}

                      {modalTab === 'clues' && (
                        <div>
                          <div className="level-progress-bar">
                            <div className="level-badge done">✓</div>
                            <div className="level-badge done">✓</div>
                            <div className="level-badge current">3</div>
                            <div className="level-badge">🔒</div>
                          </div>
                          <div style={{ fontSize: '0.65rem', fontWeight: 900, color: '#16a34a', textAlign: 'center' }}>LEVEL 3: THE GHOST IN THE LIVING ROOM</div>
                          <div className="clue-box">
                            <p className="clue-riddle">"I test friendships, press your buttons, and turn grown adults into yelling kids at 2 AM. I live right next to your TV. What am I?"</p>
                            <button className="hint-pill-btn" onClick={() => { setShowModal(false); setScreen('category'); setTutorialStep(6); }}>Hint: Check Gaming →</button>
                          </div>
                        </div>
                      )}

                      {modalTab === 'rewards' && (
                        <div className="reward-card-purple">
                          <div style={{ fontSize: '2rem' }}>🏆</div>
                          <div style={{ fontSize: '1.2rem', fontWeight: 900 }}>Prize: ₹50 OFF</div>
                          <p style={{ fontSize: '0.75rem', opacity: 0.9 }}>Unlock this mystery coupon for your next cart!</p>
                          <button className="unlock-now-btn" onClick={() => { setShowModal(false); setScreen('category'); setTutorialStep(6); }}>⚡ Unlock Now</button>
                        </div>
                      )}

                      <div className="modal-nav-bar">
                        <div id="modal-tab-walkthrough" className={`modal-nav-tab ${modalTab==='walkthrough'?'active':''}`} onClick={() => setModalTab('walkthrough')}>Walkthrough</div>
                        <div id="modal-tab-clues" className={`modal-nav-tab ${modalTab==='clues'?'active':''}`} onClick={() => setModalTab('clues')}>Clues</div>
                        <div id="modal-tab-rewards" className={`modal-nav-tab ${modalTab==='rewards'?'active':''}`} onClick={() => setModalTab('rewards')}>Rewards</div>
                      </div>
                    </div>
                  </div>
                )}

                {tutorialStep > 0 && currentStepData && (
                  <React.Fragment>
                    <div className="tutorial-overlay-mask" onClick={currentStepData.onAction} />
                    {targetRect && (
                      <div className="highlight-cutout" style={{ top: `${targetRect.top}px`, left: `${targetRect.left}px`, width: `${targetRect.width}px`, height: `${targetRect.height}px` }} />
                    )}
                    <div className="tutorial-tooltip-card" style={{ top: currentStepData.tooltipTop ? `${currentStepData.tooltipTop}px` : 'auto', bottom: currentStepData.tooltipBottom ? `${currentStepData.tooltipBottom}px` : 'auto' }}>
                      <div className="tutorial-step-badge">STEP {tutorialStep} OF 8 • GUIDED MVP TOUR</div>
                      <div className="tutorial-title">{currentStepData.title}</div>
                      <div className="tutorial-desc">{currentStepData.description}</div>
                      <div className="tutorial-btn-row">
                        <button className="btn-tut-skip" onClick={() => setTutorialStep(0)}>Skip Tour</button>
                        <button className="btn-tut-next" onClick={currentStepData.onAction}>{currentStepData.buttonText}</button>
                      </div>
                    </div>
                  </React.Fragment>
                )}
              </div>
            </div>
          </div>
        );
      }

      ReactDOM.createRoot(document.getElementById('root')).render(<App />);
    </script>
  </body>
</html>
"""

components.html(html_content, height=880, scrolling=True)
