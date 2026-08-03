"""
Frontend React 18 Mobile UI Application Component for Zepto Product Hunt.
Renders responsive Mobile Frame, Header Persona Banner, Guided Tour Cutout Overlay, Modal Card Overlay & Confetti.
"""

import streamlit.components.v1 as components
import json

RAW_HTML_TEMPLATE = """
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
      html, body {
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
        font-family: var(--font-main);
        background-color: #0f172a;
        color: var(--zepto-gray-800);
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
      }
      .app-viewport-container {
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
      }
      .mobile-device-frame {
        width: 340px;
        height: 640px;
        background: #ffffff;
        border-radius: 32px;
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.6), 0 0 0 8px #1e293b;
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
      }
      .status-bar {
        height: 36px;
        background: #0c831f;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 18px;
        font-size: 0.75rem;
        font-weight: 600;
        z-index: 40;
      }
      .phone-notch {
        position: absolute;
        top: 6px;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 20px;
        background: #000000;
        border-radius: 14px;
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
        height: 56px;
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
        font-size: 0.62rem;
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
        padding: 10px 12px 12px 12px;
        border-bottom-left-radius: 16px;
        border-bottom-right-radius: 16px;
      }
      .location-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
      .eta-pill { background: rgba(255, 255, 255, 0.25); padding: 3px 6px; border-radius: 14px; font-size: 0.7rem; font-weight: 800; }
      
      .persona-header-banner {
        background: rgba(255, 255, 255, 0.18);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 10px;
        padding: 6px 10px;
        margin-bottom: 8px;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      .search-box-wrap { position: relative; margin-bottom: 8px; }
      .search-input {
        width: 100%;
        background: white;
        border: none;
        border-radius: 10px;
        padding: 8px 10px;
        font-size: 0.78rem;
        color: var(--zepto-gray-800);
      }
      .category-chips-scroll { display: flex; gap: 5px; overflow-x: auto; padding-bottom: 2px; }
      .cat-chip {
        background: rgba(255, 255, 255, 0.2);
        color: white;
        padding: 3px 8px;
        border-radius: 14px;
        font-size: 0.68rem;
        font-weight: 600;
        white-space: nowrap;
        cursor: pointer;
      }
      .cat-chip.active { background: white; color: var(--zepto-green); font-weight: 700; }
      .cat-chip.highlight-box { border: 2px solid var(--zepto-pink); }

      .home-content-body { padding: 10px; display: flex; flex-direction: column; gap: 10px; }
      .floating-hunt-banner {
        background: linear-gradient(135deg, var(--zepto-pink), #ec4899);
        color: white;
        padding: 8px 12px;
        border-radius: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        cursor: pointer;
        box-shadow: 0 4px 14px rgba(255, 50, 105, 0.35);
      }
      .product-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; }
      .product-card {
        background: white;
        border-radius: 12px;
        padding: 8px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
        cursor: pointer;
        position: relative;
        border: 1px solid var(--zepto-gray-200);
      }
      .product-img-wrap {
        width: 100%;
        height: 85px;
        border-radius: 8px;
        overflow: hidden;
        margin-bottom: 6px;
        background: var(--zepto-gray-100);
        display: flex;
        align-items: center;
        justify-content: center;
      }
      .product-img-wrap img {
        width: 100%;
        height: 100%;
        object-fit: cover;
      }
      .product-title {
        font-size: 0.72rem;
        font-weight: 700;
        color: var(--zepto-gray-800);
        line-height: 1.2;
        height: 30px;
        overflow: hidden;
        margin-bottom: 4px;
      }
      .product-price {
        font-size: 0.8rem;
        font-weight: 900;
        color: #0f172a;
      }

      /* Modal Centered Card Overlay */
      .modal-overlay {
        position: absolute; inset: 0; background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(5px); z-index: 100; display: flex; align-items: center; justify-content: center; padding: 12px;
      }
      .modal-card {
        background: #ffffff; border-radius: 24px; padding: 16px 14px 12px 14px; width: 100%; height: 480px; position: relative; box-shadow: 0 20px 40px rgba(0,0,0,0.35); display: flex; flex-direction: column; justify-content: space-between;
      }
      .modal-close-btn {
        position: absolute; top: 12px; right: 12px; background: var(--zepto-gray-200); width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; color: #64748b; font-weight: 800; font-size: 0.75rem;
      }
      .modal-header-title { text-align: center; font-family: var(--font-display); font-weight: 800; font-size: 1.05rem; color: var(--zepto-green); margin-bottom: 8px; }
      
      .step-card { background: var(--zepto-gray-100); border-radius: 10px; padding: 8px 10px; margin-bottom: 6px; display: flex; gap: 8px; align-items: flex-start; }
      .step-icon-wrap { width: 28px; height: 28px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 0.9rem; flex-shrink: 0; }
      .step-icon-1 { background: #dcfce7; color: #15803d; }
      .step-icon-2 { background: #f3e8ff; color: #7e22ce; }
      .step-icon-3 { background: #fee2e2; color: #b91c1c; }
      .step-icon-4 { background: #dbeafe; color: #1d4ed8; }

      .modal-nav-bar { display: flex; justify-content: space-between; align-items: center; background: var(--zepto-gray-100); border-radius: 16px; padding: 4px; margin-top: 8px; position: relative; }
      .modal-nav-tab { flex: 1; text-align: center; padding: 6px 0; border-radius: 12px; font-size: 0.65rem; font-weight: 700; color: #64748b; cursor: pointer; display: flex; flex-direction: column; align-items: center; gap: 2px; }
      .modal-nav-tab.active { background: white; color: var(--zepto-green); box-shadow: 0 2px 6px rgba(0,0,0,0.08); font-weight: 800; }

      .modal-cart-btn { background: var(--zepto-pink); color: white; border-radius: 50%; width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; position: relative; cursor: pointer; margin-left: 4px; box-shadow: 0 2px 8px rgba(255, 50, 105, 0.4); flex-shrink: 0; }
      .cart-badge-num { position: absolute; top: -3px; right: -3px; background: #0c831f; color: white; font-size: 0.5rem; font-weight: 900; width: 13px; height: 13px; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 1px solid white; }

      .carousel-dots { display: flex; justify-content: center; gap: 5px; margin: 8px 0 4px 0; }
      .carousel-dot { width: 6px; height: 6px; border-radius: 50%; background: #cbd5e1; cursor: pointer; }
      .carousel-dot.active { background: #0c831f; width: 14px; border-radius: 4px; }

      .clue-progress-bar { display: flex; justify-content: center; gap: 8px; margin-bottom: 10px; }
      .clue-badge { width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.65rem; font-weight: 700; background: var(--zepto-gray-200); color: #64748b; }
      .clue-badge.done { background: var(--zepto-green); color: white; }
      .clue-badge.current { border: 2px solid var(--zepto-green); color: var(--zepto-green); }

      .clue-box { background: #f0fdf4; border: 1.5px dashed #22c55e; border-radius: 14px; padding: 12px; text-align: center; margin-bottom: 10px; }
      .clue-riddle { font-size: 0.78rem; font-weight: 600; color: var(--zepto-gray-800); line-height: 1.35; font-style: italic; margin-bottom: 8px; }
      .hint-pill-btn { background: var(--zepto-green); color: white; border: none; padding: 5px 10px; border-radius: 14px; font-size: 0.68rem; font-weight: 700; cursor: pointer; }

      .reward-card-purple { background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; border-radius: 16px; padding: 16px; text-align: center; }
      .unlock-now-btn { background: white; color: #4f46e5; border: none; width: 100%; padding: 8px; border-radius: 10px; font-size: 0.8rem; font-weight: 800; margin-top: 8px; cursor: pointer; }

      /* PDP & Cart */
      .pdp-image-box { background: white; padding: 12px; display: flex; justify-content: center; position: relative; height: 180px; }
      .pdp-image-box img { width: 100%; height: 100%; object-fit: contain; }
      .rating-badge { position: absolute; bottom: 8px; left: 10px; background: #f1f5f9; padding: 2px 5px; border-radius: 5px; font-size: 0.65rem; font-weight: 800; }
      .pdp-info-card { background: white; padding: 12px; margin-top: 4px; flex: 1; }
      .pdp-title { font-size: 0.82rem; font-weight: 800; line-height: 1.25; color: var(--zepto-gray-800); margin-bottom: 4px; }
      .sticky-bottom-add { position: absolute; bottom: 0; left: 0; right: 0; background: white; padding: 8px 12px; border-top: 1px solid var(--zepto-gray-200); display: flex; gap: 8px; align-items: center; z-index: 30; }
      .btn-add-cart-pink { flex: 1; background: var(--zepto-pink); color: white; border: none; padding: 10px; border-radius: 10px; font-size: 0.82rem; font-weight: 800; cursor: pointer; }

      .cart-hunt-card { background: #f0fdf4; border: 1.5px solid #22c55e; border-radius: 14px; padding: 10px; margin: 10px 0; text-align: center; }
      .coupon-code-badge { background: #22c55e; color: white; padding: 3px 10px; border-radius: 6px; font-weight: 900; font-size: 0.72rem; display: inline-block; margin: 4px 0; }

      /* GUIDED TUTORIAL OVERLAY */
      .tutorial-overlay-mask { position: absolute; inset: 0; background: rgba(15, 23, 42, 0.35); z-index: 200; pointer-events: none; }
      .tutorial-tooltip-card {
        position: absolute; background: white; border-radius: 14px; padding: 12px; width: calc(100% - 20px); left: 10px; box-shadow: 0 10px 25px rgba(0,0,0,0.35); z-index: 220; border: 2px solid var(--zepto-green); pointer-events: auto;
      }
      .tutorial-step-badge { background: var(--zepto-green-bg); color: var(--zepto-green); font-size: 0.6rem; font-weight: 900; padding: 2px 5px; border-radius: 6px; display: inline-block; margin-bottom: 3px; }
      .tutorial-title { font-family: var(--font-display); font-size: 0.85rem; font-weight: 800; color: var(--zepto-gray-800); margin-bottom: 2px; }
      .tutorial-desc { font-size: 0.68rem; color: #475569; line-height: 1.3; margin-bottom: 8px; }
      .tutorial-btn-row { display: flex; justify-content: space-between; align-items: center; }
      .btn-tut-skip { background: none; border: none; color: #94a3b8; font-size: 0.65rem; font-weight: 700; cursor: pointer; }
      .btn-tut-next { background: var(--zepto-green); color: white; border: none; padding: 5px 12px; border-radius: 8px; font-size: 0.7rem; font-weight: 800; cursor: pointer; }
      .highlight-cutout {
        position: absolute; border-radius: 12px; border: 3px solid var(--zepto-pink); box-shadow: 0 0 0 9999px rgba(15, 23, 42, 0.35), 0 0 16px rgba(255, 50, 105, 0.9); z-index: 210; pointer-events: none;
      }
    </style>
  </head>
  <body>
    <div id="root"></div>

    <script type="text/babel">
      const { useState, useEffect } = React;

      const INITIAL_PAYLOAD = __SESSION_PAYLOAD__;

      function App() {
        const [session, setSession] = useState(INITIAL_PAYLOAD);
        const [screen, setScreen] = useState('home');
        const [selectedCategory, setSelectedCategory] = useState('All');
        const [selectedProduct, setSelectedProduct] = useState(session.products[0]);
        const [searchQuery, setSearchQuery] = useState('');
        const [showModal, setShowModal] = useState(false);
        const [modalTab, setModalTab] = useState('walkthrough');
        const [walkthroughSlide, setWalkthroughSlide] = useState(1);
        const [cartCount, setCartCount] = useState(0);
        const [huntUnlocked, setHuntUnlocked] = useState(false);
        const [tutorialStep, setTutorialStep] = useState('__DEMO_MODE__' === 'tour' ? 1 : 0);
        const [targetRect, setTargetRect] = useState(null);

        const [currentStage, setCurrentStage] = useState(session.hunt_stage || 1);
        const [targetProd, setTargetProd] = useState(session.target_prod);
        const [liveClue, setLiveClue] = useState((session.clues_history && session.clues_history[session.hunt_stage || 1]) || session.clue);
        const [orderToast, setOrderToast] = useState(null);
        const [isGeneratingNextClue, setIsGeneratingNextClue] = useState(false);
        const [purchaseHistory, setPurchaseHistory] = useState(session.purchase_history || []);

        const currentTargetId = targetProd.id;

        useEffect(() => {
          if (tutorialStep <= 0) { setTargetRect(null); return; }
          const updateRect = () => {
            let targetId = '';
            if (tutorialStep === 1) targetId = 'nav-hunt-btn';
            else if (tutorialStep === 2) targetId = 'modal-tab-walkthrough';
            else if (tutorialStep === 3) targetId = 'modal-tab-clues';
            else if (tutorialStep === 4) targetId = 'modal-tab-rewards';
            else if (tutorialStep === 5) targetId = 'cat-chip-electronics';
            else if (tutorialStep === 6) targetId = 'product-card-mouse';
            else if (tutorialStep === 7) targetId = 'btn-add-to-cart-pdp';
            else if (tutorialStep === 8) targetId = 'cart-hunt-card-target';
            else if (tutorialStep === 9) targetId = 'product-card-gamepad';
            else if (tutorialStep === 10) targetId = 'btn-add-to-cart-pdp';
            else if (tutorialStep === 11) targetId = 'cart-hunt-card-target';

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
            case 1: return { title: "Step 1: Open Product Hunt", description: `Welcome ${session.persona.name}! Tap 'Hunt' to view your AI-generated riddle clue.`, buttonText: "Open Hunt →", tooltipBottom: 65, onAction: () => { setShowModal(true); setModalTab('walkthrough'); setTutorialStep(2); } };
            case 2: return { title: "Step 2: Walkthrough (How It Works)", description: "Review 4-step game rules: Buy Products → Unlock Clues → Find Item → Get Discount!", buttonText: "View Clue →", tooltipBottom: 130, onAction: () => { setModalTab('clues'); setTutorialStep(3); } };
            case 3: return { title: `Step 3: Read AI Clue #${currentStage}`, description: `AI Clue: "${liveClue.riddle}"`, buttonText: "Check Rewards →", tooltipBottom: 130, onAction: () => { setModalTab('rewards'); setTutorialStep(4); } };
            case 4: return { title: "Step 4: Check Prize", description: "Prize: ₹50 OFF Coupon code for your cart when you find & add the secret item!", buttonText: "Go Hunt Item →", tooltipBottom: 130, onAction: () => { setShowModal(false); setScreen('home'); setTutorialStep(5); } };
            case 5: return { title: `Step 5: Browse Category`, description: `Navigate to ${session.target_prod.category} where your target product is located.`, buttonText: `Go to ${session.target_prod.category} →`, tooltipTop: 130, onAction: () => { setScreen('category'); setSelectedCategory(session.target_prod.category); setTutorialStep(6); } };
            case 6: return { title: "Step 6: Try Non-Hunt Item (Mouse)", description: "Select Logitech G305 Mouse to test adding a normal product.", buttonText: "Open Mouse →", tooltipBottom: 65, onAction: () => { const mouseP = session.products.find(p => p.id === 'mouse') || session.products[0]; setSelectedProduct(mouseP); setScreen('pdp'); setTutorialStep(7); } };
            case 7: return { title: "Step 7: Add Mouse to Cart", description: "Tap 'Add to Cart'. Notice that the coupon will remain 🔒 LOCKED because this is not the secret hunt item!", buttonText: "Add Mouse →", tooltipBottom: 65, onAction: () => { setCartCount(1); setScreen('cart'); setTutorialStep(8); } };
            case 8: return { title: "Step 8: Coupon Remains Locked 🔒", description: "Notice ACCZ50OFF is 🔒 LOCKED. Now let's go back & find the secret hunt item!", buttonText: "Find Secret Item →", tooltipTop: 80, onAction: () => { setScreen('category'); setTutorialStep(9); } };
            case 9: return { title: "Step 9: Select Secret Hunt Item", description: `Select ${session.target_prod.name} (the item matching AI Clue #${currentStage}!).`, buttonText: "Open Target Item →", tooltipBottom: 65, onAction: () => { const targetP = session.products.find(p => p.id === currentTargetId) || session.products[0]; setSelectedProduct(targetP); setScreen('pdp'); setTutorialStep(10); } };
            case 10: return { title: "Step 10: Add Secret Item to Cart", description: "Tap 'Add to Cart' to complete the Hunt and unlock your secret discount!", buttonText: "Add Target Item →", tooltipBottom: 65, onAction: () => { setCartCount(1); setHuntUnlocked(true); setScreen('cart'); setTutorialStep(11); triggerConfetti(); } };
            case 11: return { title: "Step 11: Coupon ACCZ50OFF Unlocked! 🎉", description: `Boom! Discovered Deal + Coupon ACCZ50OFF unlocked for ${session.persona.name}!`, buttonText: "Finish Tour 🚀", tooltipTop: 80, onAction: () => { setTutorialStep(0); } };
            default: return null;
          }
        };

        const currentStepData = getTutorialStepData();

        const filteredProducts = session.products.filter(p => {
          const matchesCat = selectedCategory === 'All' || p.category === selectedCategory;
          const matchesSearch = !searchQuery || p.name.toLowerCase().includes(searchQuery.toLowerCase());
          return matchesCat && matchesSearch;
        });

        return (
          <div className="app-viewport-container">
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
                          <div style={{ fontSize: '0.52rem', opacity: 0.8, fontWeight: 700 }}>DELIVERING TO</div>
                          <div style={{ fontSize: '0.68rem', fontWeight: 700 }}>{session.persona.name} • Cyber City, Sec 24</div>
                        </div>
                        <div className="eta-pill">⚡ 6 minutes</div>
                      </div>

                      <div className="search-box-wrap">
                        <input
                          className="search-input"
                          placeholder={`Search "${session.target_prod.name.split(' ')[0]}", "Apples", "Serum"...`}
                          value={searchQuery}
                          onChange={(e) => setSearchQuery(e.target.value)}
                        />
                      </div>

                      <div className="category-chips-scroll">
                        {['All', 'Gaming', 'Fresh', 'Personal', 'Pet Store', 'Snacks'].map(cat => (
                          <div
                            key={cat}
                            id={cat === 'Gaming' ? 'cat-chip-electronics' : undefined}
                            className={`cat-chip ${selectedCategory === cat ? 'active' : ''} ${cat === session.target_prod.category && tutorialStep === 5 ? 'highlight-box' : ''}`}
                            onClick={() => {
                              setSelectedCategory(cat);
                              setScreen('category');
                              if (cat === session.target_prod.category && tutorialStep === 5) setTutorialStep(6);
                            }}
                          >
                            {cat === session.target_prod.category ? '⚡ ' : ''}{cat}
                          </div>
                        ))}
                      </div>
                    </div>

                    <div className="home-content-body">
                      {orderToast && (
                        <div style={{ background: '#0c831f', color: 'white', padding: '8px 10px', borderRadius: '10px', fontSize: '0.72rem', fontWeight: 800, textAlign: 'center', boxShadow: '0 4px 12px rgba(12, 131, 31, 0.45)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                          <span>{orderToast}</span>
                          <span style={{ cursor: 'pointer', fontWeight: 900, fontSize: '0.8rem', marginLeft: '6px' }} onClick={() => setOrderToast(null)}>✕</span>
                        </div>
                      )}
                      <div className="floating-hunt-banner" onClick={() => { setShowModal(true); setModalTab('walkthrough'); if(tutorialStep===1) setTutorialStep(2); }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <span style={{ fontSize: '1.3rem' }}>🎯</span>
                          <div>
                            <div style={{ fontSize: '0.58rem', fontWeight: 800, opacity: 0.9 }}>CLUE #{currentStage}</div>
                            <div style={{ fontSize: '0.82rem', fontWeight: 900 }}>{liveClue.clue_title || "PRODUCT HUNT WEEK"}</div>
                          </div>
                        </div>
                        <button style={{ background: 'white', color: '#ff3269', border: 'none', padding: '3px 8px', borderRadius: '12px', fontWeight: 800, fontSize: '0.68rem' }}>PLAY NOW →</button>
                      </div>

                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <div style={{ fontSize: '0.78rem', fontWeight: 900, color: '#334155' }}>Personalized Catalog ({filteredProducts.length})</div>
                        <span style={{ fontSize: '0.68rem', color: '#0c831f', fontWeight: 800, cursor: 'pointer' }} onClick={() => setScreen('category')}>View All →</span>
                      </div>

                      <div className="product-grid">
                        {filteredProducts.slice(0, 4).map(prod => (
                          <div
                            key={prod.id}
                            id={prod.id === 'gamepad' ? 'product-card-gamepad' : (prod.id === 'mouse' ? 'product-card-mouse' : undefined)}
                            className="product-card"
                            onClick={() => {
                              setSelectedProduct(prod);
                              setScreen('pdp');
                              if (prod.id === 'mouse' && tutorialStep === 6) setTutorialStep(7);
                              if (prod.id === currentTargetId && tutorialStep === 9) setTutorialStep(10);
                            }}
                          >
                            <div className="product-img-wrap">
                              <img src={prod.image} alt={prod.name} />
                            </div>
                            <div className="product-title">{prod.name}</div>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                              <div className="product-price">₹{prod.price.toLocaleString()}</div>
                              <span style={{ fontSize: '0.58rem', color: '#0c831f', fontWeight: 800 }}>Add +</span>
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>
                )}

                {screen === 'category' && (
                  <div style={{ display: 'flex', flexDirection: 'column', flex: 1, padding: '10px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '10px' }}>
                      <button style={{ background: '#e2e8f0', border: 'none', borderRadius: '50%', width: '26px', height: '26px', fontWeight: 800 }} onClick={() => setScreen('home')}>←</button>
                      <div style={{ fontSize: '0.9rem', fontWeight: 900 }}>Category: {selectedCategory}</div>
                    </div>

                    <div className="product-grid">
                      {filteredProducts.map(prod => (
                        <div
                          key={prod.id}
                          id={prod.id === 'gamepad' ? 'product-card-gamepad' : (prod.id === 'mouse' ? 'product-card-mouse' : undefined)}
                          className="product-card"
                          onClick={() => {
                            setSelectedProduct(prod);
                            setScreen('pdp');
                            if (prod.id === 'mouse' && tutorialStep === 6) setTutorialStep(7);
                            if (prod.id === currentTargetId && tutorialStep === 9) setTutorialStep(10);
                          }}
                        >
                          <div className="product-img-wrap">
                            <img src={prod.image} alt={prod.name} />
                          </div>
                          <div className="product-title">{prod.name}</div>
                          <div className="product-price">₹{prod.price.toLocaleString()}</div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {screen === 'pdp' && selectedProduct && (
                  <div style={{ display: 'flex', flexDirection: 'column', flex: 1, position: 'relative' }}>
                    <div style={{ position: 'absolute', top: '10px', left: '10px', zIndex: 20 }}>
                      <button style={{ background: 'white', border: 'none', borderRadius: '50%', width: '28px', height: '28px', fontWeight: 800, boxShadow: '0 2px 6px rgba(0,0,0,0.15)' }} onClick={() => setScreen('home')}>←</button>
                    </div>

                    <div className="pdp-image-box">
                      <img src={selectedProduct.image} alt={selectedProduct.name} />
                      <div className="rating-badge">{selectedProduct.rating}</div>
                    </div>

                    <div className="pdp-info-card">
                      <div className="pdp-title">{selectedProduct.name}</div>
                      <div style={{ fontSize: '0.68rem', color: '#64748b', marginBottom: '8px' }}>Category: {selectedProduct.category}</div>
                      <div style={{ fontSize: '1.1rem', fontWeight: 900, color: '#0f172a', marginBottom: '8px' }}>
                        ₹{selectedProduct.price.toLocaleString()}
                      </div>
                      <div style={{ fontSize: '0.72rem', color: '#334155', lineHeight: 1.4, background: '#f8fafc', padding: '8px', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
                        {selectedProduct.desc}
                      </div>
                    </div>

                    <div className="sticky-bottom-add">
                      <button
                        id="btn-add-to-cart-pdp"
                        className="btn-add-cart-pink"
                        onClick={() => {
                          setCartCount(1);
                          const isTarget = selectedProduct.id === currentTargetId;
                          if (isTarget && !huntUnlocked) {
                            setHuntUnlocked(true);
                            triggerConfetti();
                            setOrderToast(`🎉 Secret Target Found! ₹50 OFF Coupon ACCZ50OFF Unlocked!`);
                          }
                          setScreen('cart');
                          if (selectedProduct.id === 'mouse' && tutorialStep === 7) setTutorialStep(8);
                          if (isTarget && tutorialStep === 10) setTutorialStep(11);
                        }}
                      >
                        ⚡ ADD TO CART • ₹{selectedProduct.price.toLocaleString()}
                      </button>
                    </div>
                  </div>
                )}

                {screen === 'cart' && (
                  <div style={{ display: 'flex', flexDirection: 'column', flex: 1, padding: '12px', background: '#f8fafc' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '10px' }}>
                      <button style={{ background: '#e2e8f0', border: 'none', borderRadius: '50%', width: '26px', height: '26px', fontWeight: 800 }} onClick={() => setScreen('home')}>←</button>
                      <div style={{ fontSize: '0.9rem', fontWeight: 900 }}>My Cart ({cartCount} item)</div>
                    </div>

                    {selectedProduct && (
                      <div style={{ background: 'white', padding: '10px', borderRadius: '12px', display: 'flex', gap: '10px', alignItems: 'center', marginBottom: '10px', border: '1px solid #e2e8f0' }}>
                        <img src={selectedProduct.image} style={{ width: '45px', height: '45px', borderRadius: '6px', objectFit: 'cover' }} />
                        <div style={{ flex: 1 }}>
                          <div style={{ fontSize: '0.75rem', fontWeight: 800 }}>{selectedProduct.name}</div>
                          <div style={{ fontSize: '0.72rem', fontWeight: 900 }}>₹{selectedProduct.price.toLocaleString()}</div>
                        </div>
                      </div>
                    )}

                    <div id="cart-hunt-card-target" className="cart-hunt-card">
                      {huntUnlocked ? (
                        <div>
                          <div style={{ fontSize: '0.85rem', fontWeight: 900, color: '#0c831f' }}>🎉 PRODUCT HUNT COUPON UNLOCKED!</div>
                          <div className="coupon-code-badge">ACCZ50OFF APPLIED (-₹50)</div>
                          <div style={{ fontSize: '0.68rem', color: '#16a34a', fontWeight: 700, margin: '4px 0' }}>
                            Discovered Deal: ₹{selectedProduct.price.toLocaleString()} ➔ ₹{(selectedProduct.price > 1000 ? 1080 : selectedProduct.price - 50).toLocaleString()}!
                          </div>
                        </div>
                      ) : (
                        <div>
                          <div style={{ fontSize: '0.8rem', fontWeight: 800, color: '#64748b' }}>🔒 HUNT COUPON LOCKED</div>
                          <div style={{ fontSize: '0.65rem', color: '#94a3b8', margin: '3px 0' }}>
                            Coupon ACCZ50OFF is locked. Add the secret Hunt product matching AI Clue #{currentStage} to unlock!
                          </div>
                        </div>
                      )}
                    </div>

                    <div style={{ background: 'white', padding: '12px', borderRadius: '12px', marginTop: 'auto', border: '1px solid #e2e8f0' }}>
                      <div style={{ fontSize: '0.75rem', fontWeight: 900, marginBottom: '6px' }}>Bill Details</div>
                      <div style={{ display: 'flex', justifycontent: 'space-between', fontSize: '0.68rem', margin: '2px 0' }}>
                        <span>Item Total</span>
                        <span>₹{selectedProduct ? selectedProduct.price.toLocaleString() : 0}</span>
                      </div>
                      {huntUnlocked && (
                        <div style={{ display: 'flex', justifycontent: 'space-between', fontSize: '0.68rem', color: '#0c831f', fontWeight: 700, margin: '2px 0' }}>
                          <span>Hunt Discovered Coupon (ACCZ50OFF)</span>
                          <span>-₹{(selectedProduct.price > 1000 ? (selectedProduct.price - 1030) : 50).toLocaleString()}</span>
                        </div>
                      )}
                      <div style={{ display: 'flex', justifycontent: 'space-between', fontSize: '0.68rem', margin: '2px 0' }}>
                        <span>Delivery Fee</span>
                        <span style={{ color: '#0c831f', fontWeight: 800 }}>FREE</span>
                      </div>
                      <hr style={{ margin: '6px 0', borderColor: '#e2e8f0' }} />
                      <div style={{ display: 'flex', justifycontent: 'space-between', fontSize: '0.85rem', fontWeight: 900 }}>
                        <span>To Pay</span>
                        <span>₹{huntUnlocked ? (selectedProduct.price > 1000 ? 1030 : selectedProduct.price - 50).toLocaleString() : (selectedProduct ? selectedProduct.price.toLocaleString() : 0)}</span>
                      </div>
                      <button
                        style={{ width: '100%', background: '#0c831f', color: 'white', border: 'none', padding: '10px', borderRadius: '10px', fontWeight: 900, marginTop: '8px', fontSize: '0.82rem', cursor: 'pointer' }}
                        onClick={async () => {
                          const isTargetBought = selectedProduct && selectedProduct.id === currentTargetId;
                          const boughtName = selectedProduct ? selectedProduct.name : 'Item';
                          setCartCount(0);
                          setScreen('home');

                          if (currentStage < 3) {
                            const nextStage = currentStage + 1;
                            const nextTarget = session.target_prod;
                            const updatedHistory = [...purchaseHistory, boughtName];
                            setPurchaseHistory(updatedHistory);

                            // Enter Live Groq AI Loading State for Next Clue
                            setIsGeneratingNextClue(true);

                            try {
                              const apiKey = session.groq_api_key;
                              if (apiKey) {
                                const diffRule = nextStage === 2 
                                  ? "Clue 2 (Simpler Hint): Make this clue SIMPLER and MORE HELPFUL. Give a clear hint about its product category, shape, or daily usage benefit."
                                  : "Clue 3 (Direct Actionable Clue): Make this clue VERY DIRECT and EASY TO SOLVE. Explicitly point the user to the exact aisle/category!";
                                
                                const prompt = `You are the AI Game Engine for Zepto Product Hunt Week.
Generate a personalized, witty riddle clue for the customer.

USER PROFILE:
- Name: ${session.persona.name} (${session.persona.title})
- Demographics: ${session.persona.demographics}
- Tone Preference: ${session.persona.tone}
- Current Purchase History: ${updatedHistory.join(', ')}
- Suggested Adjacent Categories: ${(session.persona.suggested_categories || []).join(', ')}

TARGET PRODUCT FOR THIS HUNT STAGE:
- Name: ${nextTarget.name}
- Category: ${nextTarget.category}
- Description: ${nextTarget.desc}

CLUE PROGRESSION STAGE:
- Clue Number: ${nextStage} of 3
- Rule: ${diffRule}

STRICT JSON OUTPUT FORMAT (Return ONLY valid JSON):
{
  "clue_title": "Short 3-5 word catchphrase in ALL CAPS",
  "riddle": "1-2 sentence witty riddle matching the user tone",
  "hint": "Short 2-4 word category hint"
}`;

                                const res = await fetch("https://api.groq.com/openai/v1/chat/completions", {
                                  method: "POST",
                                  headers: {
                                    "Authorization": `Bearer ${apiKey}`,
                                    "Content-Type": "application/json"
                                  },
                                  body: JSON.stringify({
                                    model: "llama-3.1-8b-instant",
                                    messages: [{ role: "user", content: prompt }],
                                    temperature: 0.7,
                                    response_format: { type: "json_object" }
                                  })
                                });

                                if (res.ok) {
                                  const data = await res.json();
                                  const parsed = JSON.parse(data.choices[0].message.content);
                                  setLiveClue(parsed);
                                } else if (session.clues_history && session.clues_history[nextStage]) {
                                  setLiveClue(session.clues_history[nextStage]);
                                }
                              } else if (session.clues_history && session.clues_history[nextStage]) {
                                setLiveClue(session.clues_history[nextStage]);
                              }
                            } catch (err) {
                              if (session.clues_history && session.clues_history[nextStage]) {
                                setLiveClue(session.clues_history[nextStage]);
                              }
                            } finally {
                              setCurrentStage(nextStage);
                              setTargetProd(nextTarget);
                              setIsGeneratingNextClue(false);
                              if (isTargetBought) {
                                setOrderToast(`🎉 Secret Hunt Item Found! Coupon Unlocked + Clue #${nextStage} Unlocked!`);
                              } else {
                                setOrderToast(`🛒 Order Placed for ${boughtName}! Clue #${nextStage} Unlocked!`);
                              }
                              triggerConfetti();
                            }
                          } else {
                            if (isTargetBought) {
                              setOrderToast(`🏆 All 3 Hunt Challenges Completed! Grand Winner!`);
                            } else {
                              setOrderToast(`✅ Order Placed for ${boughtName}!`);
                            }
                            triggerConfetti();
                          }
                        }}
                      >
                        PROCEED TO PAY ⚡
                      </button>
                    </div>
                  </div>
                )}
              </div>

              {/* Bottom Navigation */}
              <div className="bottom-nav-bar">
                <div className={`nav-item ${screen==='home'?'active':''}`} onClick={() => setScreen('home')}>
                  <span style={{fontSize:'1rem'}}>🏠</span>
                  <span>Home</span>
                </div>
                <div className={`nav-item ${screen==='category'?'active':''}`} onClick={() => setScreen('category')}>
                  <span style={{fontSize:'1rem'}}>🛍️</span>
                  <span>Categories</span>
                </div>
                <div className={`nav-item ${screen==='cart'?'active':''}`} onClick={() => setScreen('cart')}>
                  <span style={{fontSize:'1rem'}}>🛒</span>
                  <span>Cart ({cartCount})</span>
                </div>
                <div id="nav-hunt-btn" className="nav-item hunt-highlight" onClick={() => { setShowModal(true); setModalTab('walkthrough'); if(tutorialStep===1) setTutorialStep(2); }}>
                  <span className="hunt-badge">AI LIVE</span>
                  <span style={{fontSize:'1rem'}}>🎯</span>
                  <span>🔥 Hunt</span>
                </div>
              </div>

              {/* MODAL OVERLAY CARD */}
              {showModal && (
                <div className="modal-overlay">
                  <div className="modal-card">
                    <div className="modal-close-btn" onClick={() => setShowModal(false)}>✕</div>
                    
                    <div className="modal-header-title">🎯 Zepto Product Hunt</div>

                    <div style={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
                      {modalTab === 'walkthrough' && (
                        <div style={{ display: 'flex', flexDirection: 'column', flex: 1, justifyContent: 'space-between' }}>
                          {walkthroughSlide === 1 && (
                            <div>
                              <div style={{ fontSize: '0.78rem', fontWeight: 800, textAlign: 'center', marginBottom: '8px', color: '#334155' }}>
                                How Product Hunt Works
                              </div>
                              <div className="step-card">
                                <div className="step-icon-wrap step-icon-1">🛍️</div>
                                <div>
                                  <div style={{ fontSize: '0.72rem', fontWeight: 800 }}>1. Shop & Explore</div>
                                  <div style={{ fontSize: '0.62rem', color: '#64748b' }}>Browse your favorite daily groceries & categories.</div>
                                </div>
                              </div>
                              <div className="step-card">
                                <div className="step-icon-wrap step-icon-2">🧩</div>
                                <div>
                                  <div style={{ fontSize: '0.72rem', fontWeight: 800 }}>2. AI Riddle Clues</div>
                                  <div style={{ fontSize: '0.62rem', color: '#64748b' }}>AI generates dynamic riddle clues tailored to your history!</div>
                                </div>
                              </div>
                              <div className="step-card">
                                <div className="step-icon-wrap step-icon-3">🔍</div>
                                <div>
                                  <div style={{ fontSize: '0.72rem', fontWeight: 800 }}>3. Find Secret Product</div>
                                  <div style={{ fontSize: '0.62rem', color: '#64748b' }}>Deduce the mystery product from the AI riddle.</div>
                                </div>
                              </div>
                            </div>
                          )}

                          {walkthroughSlide === 2 && (
                            <div>
                              <div className="clue-progress-bar">
                                <div className={`clue-badge ${currentStage >= 1 ? 'done' : ''}`}>1</div>
                                <div className={`clue-badge ${currentStage >= 2 ? 'done' : (currentStage === 2 ? 'current' : '')}`}>2</div>
                                <div className={`clue-badge ${currentStage === 3 ? 'current' : ''}`}>3</div>
                              </div>
                              <div style={{ fontSize: '0.58rem', fontWeight: 900, color: '#16a34a', textAlign: 'center', marginBottom: '2px' }}>
                                CLUE #{currentStage}: {liveClue.clue_title || 'MYSTERY RIDDLE'}
                              </div>
                              <div style={{ fontSize: '0.82rem', fontWeight: 900, textAlign: 'center', marginBottom: '10px' }}>Active Challenge</div>

                              <div className="clue-box">
                                <p className="clue-riddle">"{liveClue.riddle}"</p>
                              </div>
                            </div>
                          )}

                          {walkthroughSlide === 3 && (
                            <div className="reward-card-purple">
                              <div style={{ fontSize: '1.8rem' }}>🎖️</div>
                              <div style={{ fontSize: '1.15rem', fontWeight: 900, margin: '4px 0' }}>Prize: ₹50 OFF</div>
                              <p style={{ fontSize: '0.68rem', opacity: 0.9, marginBottom: '10px' }}>Unlock this mystery coupon for your next cart!</p>
                              <button className="unlock-now-btn" onClick={() => setModalTab('rewards')}>⚡ Check My Rewards</button>
                            </div>
                          )}

                          <div className="carousel-dots">
                            <span className={`carousel-dot ${walkthroughSlide===1?'active':''}`} onClick={() => setWalkthroughSlide(1)}></span>
                            <span className={`carousel-dot ${walkthroughSlide===2?'active':''}`} onClick={() => setWalkthroughSlide(2)}></span>
                            <span className={`carousel-dot ${walkthroughSlide===3?'active':''}`} onClick={() => setWalkthroughSlide(3)}></span>
                          </div>
                        </div>
                      )}

                      {modalTab === 'clues' && (
                        <div style={{ display: 'flex', flexDirection: 'column', flex: 1, justifyContent: 'space-between' }}>
                          <div style={{ overflowY: 'auto' }}>
                            <div className="clue-progress-bar">
                              <div className={`clue-badge ${currentStage >= 1 ? 'done' : ''}`}>1</div>
                              <div className={`clue-badge ${currentStage >= 2 ? 'done' : (currentStage === 2 ? 'current' : '')}`}>2</div>
                              <div className={`clue-badge ${currentStage === 3 ? 'current' : ''}`}>3</div>
                            </div>
                            <div style={{ fontSize: '0.62rem', fontWeight: 900, color: '#16a34a', textAlign: 'center', marginBottom: '6px' }}>AI CLUE PROGRESSION</div>

                            <div className="clue-box" style={{ margin: '4px 0 0 0', padding: '8px 10px' }}>
                              <div style={{ fontSize: '0.58rem', fontWeight: 900, color: '#c2410c', marginBottom: '2px' }}>🎯 CLUE #{currentStage}</div>
                              <div style={{ fontSize: '0.65rem', fontWeight: 800, color: '#16a34a', marginBottom: '2px' }}>{liveClue.clue_title}</div>
                              <p className="clue-riddle" style={{ fontSize: '0.68rem', margin: '3px 0' }}>"{liveClue.riddle}"</p>
                            </div>
                          </div>
                        </div>
                      )}

                      {modalTab === 'rewards' && (
                        <div style={{ display: 'flex', flexDirection: 'column', flex: 1, justifyContent: 'space-between' }}>
                          {huntUnlocked ? (
                            <div className="reward-card-purple" style={{ background: 'linear-gradient(135deg, #0c831f, #10b981)', padding: '16px' }}>
                              <div style={{ fontSize: '1.8rem' }}>🎉 🎖️</div>
                              <div style={{ fontSize: '1.1rem', fontWeight: 900, margin: '4px 0' }}>Prize: ₹50 OFF UNLOCKED!</div>
                              <div style={{ background: 'white', color: '#0c831f', padding: '5px 12px', borderRadius: '8px', fontWeight: 900, fontSize: '0.8rem', display: 'inline-block', margin: '8px 0' }}>
                                COUPON CODE: ACCZ50OFF
                              </div>
                              <p style={{ fontSize: '0.68rem', opacity: 0.95, margin: '4px 0' }}>Congratulations {session.persona.name}! Coupon auto-applied.</p>
                              <button className="unlock-now-btn" style={{ color: '#0c831f', marginTop: '10px' }} onClick={() => { setShowModal(false); setScreen('cart'); }}>⚡ View Cart & Pay</button>
                            </div>
                          ) : (
                            <div style={{ background: '#f8fafc', border: '1.5px dashed #cbd5e1', borderRadius: '16px', padding: '16px', textAlign: 'center', color: '#64748b' }}>
                              <div style={{ fontSize: '1.8rem' }}>🔒</div>
                              <div style={{ fontSize: '1.05rem', fontWeight: 900, color: '#334155', margin: '4px 0' }}>Prize: ₹50 OFF</div>
                              <div style={{ background: '#e2e8f0', color: '#64748b', padding: '5px 12px', borderRadius: '8px', fontWeight: 800, fontSize: '0.78rem', display: 'inline-block', margin: '8px 0', filter: 'blur(3px)', userSelect: 'none' }}>
                                COUPON: ACCZ50OFF
                              </div>
                              <p style={{ fontSize: '0.68rem', color: '#64748b', margin: '6px 0' }}>Add the secret product matching AI Clue #{currentStage} to your cart to unlock!</p>
                              <button disabled style={{ background: '#e2e8f0', color: '#94a3b8', border: 'none', width: '100%', padding: '8px', borderRadius: '10px', fontSize: '0.78rem', fontWeight: 800, marginTop: '10px', cursor: 'not-allowed' }}>
                                🔒 Locked (Find Target Item to Unlock)
                              </button>
                            </div>
                          )}
                        </div>
                      )}

                      <div className="modal-nav-bar">
                        <div id="modal-tab-walkthrough" className={`modal-nav-tab ${modalTab==='walkthrough'?'active':''}`} onClick={() => setModalTab('walkthrough')}>
                          <span style={{fontSize:'0.85rem'}}>🔍</span>
                          <span>Walkthrough</span>
                        </div>
                        <div id="modal-tab-clues" className={`modal-nav-tab ${modalTab==='clues'?'active':''}`} onClick={() => setModalTab('clues')}>
                          <span style={{fontSize:'0.85rem'}}>🛍️</span>
                          <span>My Clues</span>
                        </div>
                        <div id="modal-tab-rewards" className={`modal-nav-tab ${modalTab==='rewards'?'active':''}`} onClick={() => setModalTab('rewards')}>
                          <span style={{fontSize:'0.85rem'}}>🎁</span>
                          <span>My Rewards</span>
                        </div>
                        <div className="modal-cart-btn" onClick={() => { setShowModal(false); setScreen('cart'); }}>
                          <span style={{fontSize:'0.75rem'}}>🛒</span>
                          <span className="cart-badge-num">{cartCount || 0}</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              )}

                {tutorialStep > 0 && currentStepData && (
                  <React.Fragment>
                    <div className="tutorial-overlay-mask" />
                    {targetRect && (
                      <div className="highlight-cutout" style={{ top: `${targetRect.top}px`, left: `${targetRect.left}px`, width: `${targetRect.width}px`, height: `${targetRect.height}px` }} />
                    )}
                    <div className="tutorial-tooltip-card" style={{ top: currentStepData.tooltipTop ? `${currentStepData.tooltipTop}px` : 'auto', bottom: currentStepData.tooltipBottom ? `${currentStepData.tooltipBottom}px` : 'auto' }}>
                      <div className="tutorial-step-badge">STEP {tutorialStep} OF 11 • GUIDED MVP TOUR</div>
                      <div className="tutorial-title">{currentStepData.title}</div>
                      <div className="tutorial-desc">{currentStepData.description}</div>
                      <div className="tutorial-btn-row">
                        <button className="btn-tut-skip" onClick={() => setTutorialStep(0)}>Skip Tour</button>
                        <button className="btn-tut-next" onClick={currentStepData.onAction}>{currentStepData.buttonText}</button>
                      </div>
                    </div>
                  </React.Fragment>
                )}

                {isGeneratingNextClue && (
                  <div className="modal-overlay" style={{ background: 'rgba(15, 23, 42, 0.88)', zIndex: 300, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                    <div style={{ background: 'white', borderRadius: '20px', padding: '24px 18px', textAlign: 'center', width: '260px', boxShadow: '0 20px 40px rgba(0,0,0,0.5)' }}>
                      <div style={{ fontSize: '2.2rem', marginBottom: '8px' }}>⚡</div>
                      <div style={{ fontSize: '0.92rem', fontWeight: 900, color: '#0c831f', marginBottom: '4px' }}>
                        Groq AI Generating Clue #{currentStage + 1}...
                      </div>
                      <div style={{ fontSize: '0.66rem', color: '#475569', lineHeight: 1.4, margin: '6px 0' }}>
                        Analyzing updated purchase history and crafting personalized riddle for {session.persona.name}...
                      </div>
                    </div>
                  </div>
                )}
              </div>
            </div>
          );
      }

      ReactDOM.createRoot(document.getElementById('root')).render(<App />);
    </script>
  </body>
</html>
"""

def render_react_mobile_app(react_session_payload, demo_mode):
    """Render the React Mobile Application inside Streamlit viewport."""
    payload_json = json.dumps(react_session_payload)
    final_html = RAW_HTML_TEMPLATE.replace("__SESSION_PAYLOAD__", payload_json).replace("__DEMO_MODE__", demo_mode)
    components.html(final_html, height=650, scrolling=False)
