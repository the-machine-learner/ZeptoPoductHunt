import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Zepto Product Hunt - Gamified Discovery MVP",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Streamlit Shell to remove top padding, header, & eliminate scrollbars
st.markdown("""
<style>
    header[data-testid="stHeader"] {
        display: none !important;
    }
    [data-testid="stAppViewContainer"] {
        padding: 0 !important;
        background-color: #0f172a !important;
        overflow: hidden !important;
    }
    .main .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
        margin-top: 0 !important;
    }
    iframe {
        display: block;
        margin: 0 auto;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# Manage Demo State in Streamlit Session State
if "demo_mode" not in st.session_state:
    st.session_state.demo_mode = "normal"
if "demo_key" not in st.session_state:
    st.session_state.demo_key = 0

# Sidebar Setup with Controls Shifted to Top
st.sidebar.title("🎯 Zepto Product Hunt")
st.sidebar.markdown("**Gamified Category Discovery Engine MVP**")

st.sidebar.markdown("### 🎮 Demo Controls")
col1, col2 = st.sidebar.columns(2)
if col1.button("🔄 Reset Demo", use_container_width=True):
    st.session_state.demo_mode = "normal"
    st.session_state.demo_key += 1
if col2.button("▶ Start Tour", use_container_width=True):
    st.session_state.demo_mode = "tour"
    st.session_state.demo_key += 1

st.sidebar.markdown("---")
st.sidebar.info("""
**Interactive Flow Steps:**
1. **Screen 1 (Home)**: Tap **🔥 Hunt** at bottom right or browse categories.
2. **Screen 2 (Walkthrough)**: View 4-step game rules.
3. **Screen 3 (Clue Challenge)**: Read Level 3 riddle (*"I test friendships, press your buttons..."*).
4. **Screen 4 (Rewards)**: Check Prize ₹50 OFF.
5. **Screen 5 (Category)**: Browse real products with stock photos.
6. **Screen 6 (PDP)**: Open Zebronics MAX FURY RGB Gamepad & tap **Add to Cart**.
7. **Screen 7 (Cart)**: View unlocked Coupon Code `ACCZ50OFF` + Celebration Banner!
""")

st.sidebar.caption("Built for Product Management Showcase • Gen Z Discovery Engine")

raw_html_template = """
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
      body {
        font-family: var(--font-main);
        background-color: #0f172a;
        color: var(--zepto-gray-800);
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        overflow: hidden;
      }
      .app-viewport-container {
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
      .product-mrp {
        font-size: 0.62rem;
        text-decoration: line-through;
        color: #94a3b8;
        margin-left: 4px;
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

      .level-progress-bar { display: flex; justify-content: center; gap: 8px; margin-bottom: 10px; }
      .level-badge { width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.65rem; font-weight: 700; background: var(--zepto-gray-200); color: #64748b; }
      .level-badge.done { background: var(--zepto-green); color: white; }
      .level-badge.current { border: 2px solid var(--zepto-green); color: var(--zepto-green); }

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

      const PRODUCTS = [
        {
          id: 'gamepad',
          name: 'Zebronics MAX FURY RGB Gamepad',
          category: 'Gaming',
          price: 1999,
          rating: '4.8 ★ (1.2k)',
          isHuntItem: true,
          image: 'https://images.unsplash.com/photo-1600080972464-8e5f35f63d08?w=400&auto=format&fit=crop',
          desc: 'Transparent RGB LED Wired Gamepad | Dual Motor Force Feedback | Ultra-low Latency 1.8m Cable'
        },
        {
          id: 'headphones',
          name: 'Sony WH-1000XM5 ANC Headphones',
          category: 'Gaming',
          price: 29990,
          rating: '4.9 ★ (3.1k)',
          isHuntItem: false,
          image: 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&auto=format&fit=crop',
          desc: 'Industry Leading Noise Cancellation | 30hr Battery Life | Crystal Clear Hands-free Calls'
        },
        {
          id: 'mouse',
          name: 'Logitech G305 Wireless Mouse',
          category: 'Gaming',
          price: 4295,
          rating: '4.7 ★ (890)',
          isHuntItem: false,
          image: 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400&auto=format&fit=crop',
          desc: 'LIGHTSPEED Wireless Technology | HERO Sensor 12,000 DPI | 250 Hours Battery Life'
        },
        {
          id: 'apples',
          name: 'Organic Shimla Apples (4 pcs)',
          category: 'Fresh',
          price: 189,
          rating: '4.7 ★ (4.1k)',
          isHuntItem: false,
          image: 'https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=400&auto=format&fit=crop',
          desc: 'Crisp, Juicy, Farm-Fresh High Mountain Shimla Apples (~500g)'
        },
        {
          id: 'avocado',
          name: 'Fresh Imported Hass Avocado (2 pcs)',
          category: 'Fresh',
          price: 260,
          rating: '4.5 ★ (920)',
          isHuntItem: false,
          image: 'https://images.unsplash.com/photo-1523049673857-eb18f1d7b578?w=400&auto=format&fit=crop',
          desc: 'Nutrient Rich Ready-to-Eat Premium Imported Hass Avocados'
        },
        {
          id: 'cerave',
          name: 'CeraVe Hydrating Cleanser (236ml)',
          category: 'Personal',
          price: 550,
          rating: '4.8 ★ (2.8k)',
          isHuntItem: false,
          image: 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400&auto=format&fit=crop',
          desc: 'Non-Foaming Face Wash with Essential Ceramides & Hyaluronic Acid'
        },
        {
          id: 'serum',
          name: 'Minimalist 10% Vitamin C Serum',
          category: 'Personal',
          price: 699,
          rating: '4.7 ★ (1.5k)',
          isHuntItem: false,
          image: 'https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400&auto=format&fit=crop',
          desc: 'Glow Boosting Formula with Centella Water & Acetyl Glucosamine (30ml)'
        },
        {
          id: 'pedigree',
          name: 'Pedigree Adult Dog Food (3kg)',
          category: 'Pet Store',
          price: 920,
          rating: '4.8 ★ (1.1k)',
          isHuntItem: false,
          image: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=400&auto=format&fit=crop',
          desc: '100% Complete Nutrition for Adult Dogs | Healthy Coat & Digestion'
        },
        {
          id: 'doritos',
          name: 'Doritos Nacho Cheese Chips (150g)',
          category: 'Snacks',
          price: 90,
          rating: '4.9 ★ (8.9k)',
          isHuntItem: false,
          image: 'https://images.unsplash.com/photo-1566478989037-eec170784d0b?w=400&auto=format&fit=crop',
          desc: 'Crunchy Tortilla Chips with Bold & Cheesy Nacho Flavor'
        }
      ];

      function App() {
        const [screen, setScreen] = useState('home');
        const [selectedCategory, setSelectedCategory] = useState('All');
        const [selectedProduct, setSelectedProduct] = useState(PRODUCTS[0]);
        const [searchQuery, setSearchQuery] = useState('');
        const [showModal, setShowModal] = useState(false);
        const [modalTab, setModalTab] = useState('walkthrough');
        const [walkthroughSlide, setWalkthroughSlide] = useState(1);
        const [cartCount, setCartCount] = useState(0);
        const [huntUnlocked, setHuntUnlocked] = useState(false);
        const [tutorialStep, setTutorialStep] = useState('__DEMO_MODE__' === 'tour' ? 1 : 0);
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
            case 1: return { title: "Step 1: Open Product Hunt", description: "Tap the highlighted 'Hunt' icon at the bottom right to enter Product Hunt Week!", buttonText: "Open Hunt →", tooltipBottom: 65, onAction: () => { setShowModal(true); setModalTab('walkthrough'); setTutorialStep(2); } };
            case 2: return { title: "Step 2: Walkthrough (How It Works)", description: "Review 4-step game rules: Buy Products → Unlock Clues → Find Item → Get Discount!", buttonText: "View Clue →", tooltipBottom: 130, onAction: () => { setModalTab('clues'); setTutorialStep(3); } };
            case 3: return { title: "Step 3: Read Spicy AI Clue", description: "Level 3 Challenge: 'I test friendships, press your buttons... next to your TV.' Hint: Gaming!", buttonText: "Check Rewards →", tooltipBottom: 130, onAction: () => { setModalTab('rewards'); setTutorialStep(4); } };
            case 4: return { title: "Step 4: Check Prize", description: "Prize: ₹50 OFF Coupon code for your cart when you find & add the secret item!", buttonText: "Go Hunt Item →", tooltipBottom: 130, onAction: () => { setShowModal(false); setScreen('home'); setTutorialStep(5); } };
            case 5: return { title: "Step 5: Browse Category", description: "Navigate to Gaming where the products are located.", buttonText: "Go to Gaming →", tooltipTop: 130, onAction: () => { setScreen('category'); setSelectedCategory('Gaming'); setTutorialStep(6); } };
            case 6: return { title: "Step 6: Try Non-Hunt Item (Mouse)", description: "Select Logitech G305 Wireless Mouse to test adding a normal product.", buttonText: "Open Mouse →", tooltipBottom: 65, onAction: () => { setSelectedProduct(PRODUCTS[2]); setScreen('pdp'); setTutorialStep(7); } };
            case 7: return { title: "Step 7: Add Mouse to Cart", description: "Tap 'Add to Cart'. Notice that the coupon will remain 🔒 LOCKED because this is not the hunt item!", buttonText: "Add Mouse →", tooltipBottom: 65, onAction: () => { setCartCount(1); setScreen('cart'); setTutorialStep(8); } };
            case 8: return { title: "Step 8: Coupon Remains Locked 🔒", description: "Notice ACCZ50OFF is 🔒 LOCKED (Full price ₹4,295). Now let's go back & find the real secret hunt item!", buttonText: "Find Secret Item →", tooltipTop: 80, onAction: () => { setScreen('category'); setTutorialStep(9); } };
            case 9: return { title: "Step 9: Select Secret Hunt Item", description: "Select Zebronics MAX FURY RGB Gamepad (the item matching the Level 3 AI clue!).", buttonText: "Open Gamepad →", tooltipBottom: 65, onAction: () => { setSelectedProduct(PRODUCTS[0]); setScreen('pdp'); setTutorialStep(10); } };
            case 10: return { title: "Step 10: Add Secret Item to Cart", description: "Tap 'Add to Cart' to complete the Hunt and unlock your secret discount!", buttonText: "Add Gamepad →", tooltipBottom: 65, onAction: () => { setCartCount(1); setHuntUnlocked(true); setScreen('cart'); setTutorialStep(11); triggerConfetti(); } };
            case 11: return { title: "Step 11: Coupon ACCZ50OFF Unlocked! 🎉", description: "Boom! Discovered Deal (-₹919) + Coupon ACCZ50OFF (-₹50) unlocked! Total: ₹1,030!", buttonText: "Finish Tour 🚀", tooltipTop: 80, onAction: () => { setTutorialStep(0); } };
            default: return null;
          }
        };

        const currentStepData = getTutorialStepData();

        const filteredProducts = PRODUCTS.filter(p => {
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
                          <div style={{ fontSize: '0.55rem', opacity: 0.8, fontWeight: 700 }}>DELIVERING TO</div>
                          <div style={{ fontSize: '0.72rem', fontWeight: 700 }}>Home • Cyber City, Sector 24...</div>
                        </div>
                        <div className="eta-pill">⚡ 6 minutes</div>
                      </div>

                      <div className="search-box-wrap">
                        <input
                          className="search-input"
                          placeholder='Search "Gamepad", "Apples", "Serum"...'
                          value={searchQuery}
                          onChange={(e) => setSearchQuery(e.target.value)}
                        />
                      </div>

                      <div className="category-chips-scroll">
                        {['All', 'Gaming', 'Fresh', 'Personal', 'Pet Store', 'Snacks'].map(cat => (
                          <div
                            key={cat}
                            id={cat === 'Gaming' ? 'cat-chip-electronics' : undefined}
                            className={`cat-chip ${selectedCategory === cat ? 'active' : ''} ${cat === 'Gaming' && tutorialStep === 5 ? 'highlight-box' : ''}`}
                            onClick={() => {
                              setSelectedCategory(cat);
                              setScreen('category');
                              if (cat === 'Gaming' && tutorialStep === 5) setTutorialStep(6);
                            }}
                          >
                            {cat === 'Gaming' ? '⚡ ' : ''}{cat}
                          </div>
                        ))}
                      </div>
                    </div>

                    <div className="home-content-body">
                      <div className="floating-hunt-banner" onClick={() => { setShowModal(true); setModalTab('walkthrough'); if(tutorialStep===1) setTutorialStep(2); }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <span style={{ fontSize: '1.3rem' }}>🎯</span>
                          <div>
                            <div style={{ fontSize: '0.62rem', fontWeight: 800, opacity: 0.9 }}>LIMITED TIME EVENT</div>
                            <div style={{ fontSize: '0.85rem', fontWeight: 900 }}>PRODUCT HUNT WEEK</div>
                          </div>
                        </div>
                        <button style={{ background: 'white', color: '#ff3269', border: 'none', padding: '3px 8px', borderRadius: '12px', fontWeight: 800, fontSize: '0.68rem' }}>PLAY NOW →</button>
                      </div>

                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <div style={{ fontSize: '0.8rem', fontWeight: 900, color: '#334155' }}>Trending Catalog ({filteredProducts.length})</div>
                        <span style={{ fontSize: '0.68rem', color: '#0c831f', fontWeight: 800, cursor: 'pointer' }} onClick={() => setScreen('category')}>View All →</span>
                      </div>

                      <div className="product-grid">
                        {filteredProducts.slice(0, 4).map(prod => (
                          <div
                            key={prod.id}
                            id={prod.id === 'gamepad' ? 'product-card-gamepad' : undefined}
                            className="product-card"
                            onClick={() => {
                              setSelectedProduct(prod);
                              setScreen('pdp');
                              if (prod.id === 'gamepad' && tutorialStep === 6) setTutorialStep(7);
                            }}
                          >
                            <div className="product-img-wrap">
                              <img src={prod.image} alt={prod.name} />
                            </div>
                            <div className="product-title">{prod.name}</div>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '3px' }}>
                              <div className="product-price">
                                ₹{prod.price}
                              </div>
                              <button style={{ background: '#0c831f', color: 'white', border: 'none', padding: '3px 6px', borderRadius: '6px', fontSize: '0.65rem', fontWeight: 800 }}>ADD</button>
                            </div>
                          </div>
                        ))}
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
                  <div style={{ display: 'flex', flexDirection: 'column', flex: 1, padding: '10px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '10px' }}>
                      <button onClick={() => setScreen('home')} style={{ border: 'none', background: 'none', fontSize: '1.1rem', cursor: 'pointer' }}>←</button>
                      <input className="search-input" value={selectedCategory + " Category Catalog"} readOnly style={{ background: '#e2e8f0' }} />
                    </div>

                    <div style={{ display: 'flex', gap: '5px', overflowX: 'auto', marginBottom: '10px' }}>
                      {['All', 'Gaming', 'Fresh', 'Personal', 'Pet Store', 'Snacks'].map(cat => (
                        <div
                          key={cat}
                          className={`cat-chip ${selectedCategory === cat ? 'active' : ''}`}
                          style={{ color: selectedCategory === cat ? '#0c831f' : '#64748b', background: selectedCategory === cat ? '#e6f4ea' : '#f1f5f9' }}
                          onClick={() => setSelectedCategory(cat)}
                        >
                          {cat}
                        </div>
                      ))}
                    </div>

                    <div className="product-grid" style={{ flex: 1, overflowY: 'auto' }}>
                      {filteredProducts.map(prod => (
                        <div
                          key={prod.id}
                          id={prod.id === 'mouse' ? 'product-card-mouse' : (prod.id === 'gamepad' ? 'product-card-gamepad' : undefined)}
                          className="product-card"
                          onClick={() => {
                            setSelectedProduct(prod);
                            setScreen('pdp');
                            if (prod.id === 'mouse' && tutorialStep === 6) setTutorialStep(7);
                            if (prod.id === 'gamepad' && tutorialStep === 9) setTutorialStep(10);
                          }}
                        >
                          <div className="product-img-wrap">
                            <img src={prod.image} alt={prod.name} />
                          </div>
                          <div className="product-title">{prod.name}</div>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '3px' }}>
                            <div className="product-price">
                              ₹{prod.price}
                            </div>
                            <button style={{ background: '#0c831f', color: 'white', border: 'none', padding: '3px 6px', borderRadius: '6px', fontSize: '0.65rem', fontWeight: 800 }}>ADD</button>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {screen === 'pdp' && selectedProduct && (
                  <div style={{ display: 'flex', flexDirection: 'column', flex: 1, position: 'relative' }}>
                    <div style={{ padding: '8px 10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <button onClick={() => setScreen('category')} style={{ border: 'none', background: 'none', fontSize: '0.9rem', fontWeight: 700, cursor: 'pointer' }}>← Back</button>
                      <span style={{ fontSize: '0.7rem', fontWeight: 800, color: '#0c831f' }}>⚡ 6 MINS DELIVERY</span>
                    </div>
                    <div className="pdp-image-box">
                      <img src={selectedProduct.image} alt={selectedProduct.name} />
                      <div className="rating-badge">{selectedProduct.rating}</div>
                    </div>
                    <div className="pdp-info-card">
                      <div className="pdp-title">{selectedProduct.name}</div>
                      <p style={{ fontSize: '0.7rem', color: '#64748b', marginBottom: '8px' }}>{selectedProduct.desc}</p>
                      <div style={{ fontSize: '1.1rem', fontWeight: 900 }}>
                        ₹{selectedProduct.price}
                      </div>
                    </div>
                    <div className="sticky-bottom-add">
                      <button
                        id="btn-add-to-cart-pdp"
                        className="btn-add-cart-pink"
                        onClick={() => {
                          setCartCount(1);
                          setScreen('cart');
                          if (selectedProduct.isHuntItem) {
                            setHuntUnlocked(true);
                            if (tutorialStep === 10) {
                              setTutorialStep(11);
                              triggerConfetti();
                            }
                          } else {
                            if (tutorialStep === 7) {
                              setTutorialStep(8);
                            }
                          }
                        }}
                      >
                        Add to Cart • ₹{selectedProduct.price}
                      </button>
                    </div>
                  </div>
                )}

                {screen === 'cart' && (
                  <div style={{ display: 'flex', flexDirection: 'column', flex: 1, overflowY: 'auto', paddingBottom: '60px', background: '#f1f5f9' }}>
                    {/* Cart Top Header */}
                    <div style={{ background: 'white', padding: '6px 10px', display: 'flex', alignItems: 'center', gap: '8px', borderBottom: '1px solid #e2e8f0' }}>
                      <button onClick={() => setScreen('category')} style={{ border: 'none', background: 'none', fontSize: '0.9rem', fontWeight: 800, cursor: 'pointer' }}>←</button>
                      <div>
                        <div style={{ fontSize: '0.72rem', fontWeight: 900 }}>Home 📍</div>
                        <div style={{ fontSize: '0.55rem', color: '#64748b' }}>Flat 1002, Building A, Cyber City...</div>
                      </div>
                    </div>

                    {/* Savings Alert Banner */}
                    <div style={{ background: '#dcfce7', color: '#15803d', padding: '5px 10px', fontSize: '0.62rem', fontWeight: 800, textAlign: 'center' }}>
                      🎉 Yay! You saved ₹{selectedProduct.mrp - selectedProduct.price + 50} on this order
                    </div>

                    {/* Coupons & Offers Card */}
                    <div style={{ background: 'white', margin: '4px 0', padding: '6px 10px' }}>
                      <div style={{ fontSize: '0.65rem', fontWeight: 800, color: '#475569', marginBottom: '4px' }}>Coupons & Offers</div>
                      {(huntUnlocked || selectedProduct.isHuntItem) ? (
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: '#f0fdf4', border: '1px dashed #22c55e', padding: '5px 8px', borderRadius: '8px', marginBottom: '4px' }}>
                          <div>
                            <div style={{ fontSize: '0.62rem', fontWeight: 900, color: '#16a34a' }}>Save ₹50 with ACCZ50OFF</div>
                            <div style={{ fontSize: '0.52rem', color: '#64748b' }}>Product Hunt Unlocked Reward</div>
                          </div>
                          <span style={{ background: '#22c55e', color: 'white', fontSize: '0.55rem', fontWeight: 900, padding: '2px 6px', borderRadius: '6px' }}>Applied ✓</span>
                        </div>
                      ) : (
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: '#f8fafc', border: '1px dashed #cbd5e1', padding: '5px 8px', borderRadius: '8px', marginBottom: '4px' }}>
                          <div>
                            <div style={{ fontSize: '0.62rem', fontWeight: 800, color: '#64748b' }}>Save ₹50 with ACCZ50OFF</div>
                            <div style={{ fontSize: '0.52rem', color: '#94a3b8' }}>🔒 Find secret item in Gaming to unlock</div>
                          </div>
                          <span style={{ color: '#94a3b8', fontSize: '0.55rem', fontWeight: 800 }}>Locked 🔒</span>
                        </div>
                      )}
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: '#f8fafc', border: '1px solid #e2e8f0', padding: '5px 8px', borderRadius: '8px' }}>
                        <div>
                          <div style={{ fontSize: '0.62rem', fontWeight: 800, color: '#334155' }}>Save ₹40 with CRAZE40</div>
                          <div style={{ fontSize: '0.52rem', color: '#64748b' }}>On orders above ₹499</div>
                        </div>
                        <span style={{ color: '#ff3269', fontSize: '0.55rem', fontWeight: 800, cursor: 'pointer' }}>Apply</span>
                      </div>
                    </div>

                    {/* Delivery Info */}
                    <div style={{ background: 'white', margin: '0 0 4px 0', padding: '6px 10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <div>
                        <div style={{ fontSize: '0.65rem', fontWeight: 900, color: '#0f172a' }}>⚡ Delivery in 10 mins</div>
                        <div style={{ fontSize: '0.55rem', color: '#64748b' }}>Superfast Express Delivery</div>
                      </div>
                      <span style={{ fontSize: '0.58rem', fontWeight: 800, color: '#0c831f' }}>Schedule →</span>
                    </div>

                    {/* Cart Item Row */}
                    <div style={{ background: 'white', padding: '6px 10px', marginBottom: '4px' }}>
                      <div style={{ fontSize: '0.65rem', fontWeight: 800, color: '#475569', marginBottom: '4px' }}>Cart Item</div>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <img src={selectedProduct.image} alt={selectedProduct.name} style={{ width: '36px', height: '36px', objectFit: 'contain', borderRadius: '6px' }} />
                        <div style={{ flex: 1 }}>
                          <div style={{ fontSize: '0.65rem', fontWeight: 800, color: '#0f172a', lineHeight: 1.2 }}>{selectedProduct.name}</div>
                          <div style={{ fontSize: '0.62rem', fontWeight: 900, color: '#0f172a', marginTop: '2px' }}>
                            ₹{selectedProduct.price} <span style={{ fontSize: '0.52rem', textDecoration: 'line-through', color: '#94a3b8' }}>₹{selectedProduct.mrp}</span>
                          </div>
                        </div>
                        {/* Quantity Counter */}
                        <div style={{ display: 'flex', alignItems: 'center', border: '1px solid #cbd5e1', borderRadius: '6px', background: '#f8fafc' }}>
                          <button style={{ border: 'none', background: 'none', padding: '1px 5px', fontWeight: 900, fontSize: '0.7rem', cursor: 'pointer' }}>-</button>
                          <span style={{ fontSize: '0.62rem', fontWeight: 800, padding: '0 3px' }}>1</span>
                          <button style={{ border: 'none', background: 'none', padding: '1px 5px', fontWeight: 900, fontSize: '0.7rem', cursor: 'pointer' }}>+</button>
                        </div>
                      </div>
                      <div style={{ fontSize: '0.55rem', color: '#ff3269', fontWeight: 700, marginTop: '4px', cursor: 'pointer' }}>+ Add 1 More Item</div>
                    </div>

                    {/* Bill Details */}
                    <div style={{ background: 'white', padding: '6px 10px', marginBottom: '4px' }}>
                      <div style={{ fontSize: '0.65rem', fontWeight: 800, color: '#475569', marginBottom: '4px' }}>Bill Details</div>
                      <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.58rem', color: '#64748b', marginBottom: '2px' }}>
                        <span>Item Regular Price</span>
                        <span>₹{selectedProduct.price}</span>
                      </div>
                      {selectedProduct.isHuntItem && (
                        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.58rem', color: '#16a34a', marginBottom: '2px' }}>
                          <span>Product Hunt Discovered Deal (₹1999 → ₹1080)</span>
                          <span>-₹919</span>
                        </div>
                      )}
                      {(huntUnlocked || selectedProduct.isHuntItem) && (
                        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.58rem', color: '#16a34a', marginBottom: '2px' }}>
                          <span>Hunt Level 3 Coupon (ACCZ50OFF)</span>
                          <span>-₹50</span>
                        </div>
                      )}
                      <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.58rem', color: '#64748b', marginBottom: '3px' }}>
                        <span>Delivery Fee</span>
                        <span style={{ color: '#16a34a', fontWeight: 800 }}>FREE</span>
                      </div>
                      <div style={{ borderTop: '1px dashed #cbd5e1', paddingTop: '3px', display: 'flex', justifyContent: 'space-between', fontSize: '0.7rem', fontWeight: 900, color: '#0f172a' }}>
                        <span>To Pay</span>
                        <span>
                          ₹{selectedProduct.isHuntItem
                              ? 1030
                              : ((huntUnlocked) ? Math.max(0, selectedProduct.price - 50) : selectedProduct.price)
                           }
                        </span>
                      </div>
                    </div>

                    {/* Product Hunt Card */}
                    <div className="cart-hunt-card" id="cart-hunt-card-target" style={{ margin: '4px 10px 10px 10px', padding: '8px' }}>
                      <div className="level-progress-bar" style={{ marginBottom: '4px' }}>
                        <div className="level-badge done">✓</div>
                        <div className="level-badge done">✓</div>
                        <div className={`level-badge ${huntUnlocked || selectedProduct.isHuntItem ? 'done' : 'current'}`} style={{ background: (huntUnlocked || selectedProduct.isHuntItem) ? '#22c55e' : undefined }}>
                          {(huntUnlocked || selectedProduct.isHuntItem) ? '✓' : '3'}
                        </div>
                      </div>
                      <div className="coupon-code-badge" style={{ fontSize: '0.65rem' }}>
                        {(huntUnlocked || selectedProduct.isHuntItem) ? 'COUPON CODE: ACCZ50OFF' : 'COUPON CODE: ACCZ**** (LOCKED)'}
                      </div>
                      <div style={{ fontSize: '0.85rem', fontWeight: 900, color: (huntUnlocked || selectedProduct.isHuntItem) ? '#15803d' : '#ea580c' }}>
                        {(huntUnlocked || selectedProduct.isHuntItem) ? 'Congratulations !!! 🎉' : '🎯 Level 3 Hunt In Progress'}
                      </div>
                      <div style={{ fontSize: '0.62rem', color: (huntUnlocked || selectedProduct.isHuntItem) ? '#166534' : '#475569' }}>
                        {(huntUnlocked || selectedProduct.isHuntItem)
                          ? 'Level 3 Complete! You unlocked ₹50 OFF + Free Delivery on this order.'
                          : 'Find the secret item in Gaming & add to cart to unlock ₹50 OFF coupon!'}
                      </div>
                    </div>

                    {/* Sticky Bottom Bar */}
                    <div className="sticky-bottom-add" style={{ padding: '6px 10px', background: 'white', borderTop: '1px solid #e2e8f0' }}>
                      <div style={{ flex: 1 }}>
                        <div style={{ fontSize: '0.52rem', color: '#64748b' }}>Pay via PhonePe / UPI</div>
                        <div style={{ fontSize: '0.78rem', fontWeight: 900, color: '#0f172a' }}>
                          ₹{selectedProduct.isHuntItem
                              ? 1030
                              : ((huntUnlocked) ? Math.max(0, selectedProduct.price - 50) : selectedProduct.price)
                           }
                        </div>
                      </div>
                      <button className="btn-add-cart-pink" style={{ flex: 'none', width: '120px', padding: '7px', fontSize: '0.75rem' }} onClick={() => alert('🎉 Order Placed Successfully!')}>
                        Pay ₹{selectedProduct.isHuntItem
                              ? 1030
                              : ((huntUnlocked) ? Math.max(0, selectedProduct.price - 50) : selectedProduct.price)
                           }
                      </button>
                    </div>
                  </div>
                )}

                {showModal && (
                  <div className="modal-overlay">
                    <div className="modal-card">
                      <div className="modal-close-btn" onClick={() => setShowModal(false)}>✕</div>
                      <div className="modal-header-title" style={{ marginBottom: '2px' }}>PRODUCT HUNT WEEK</div>
                      <div style={{ fontSize: '0.62rem', fontWeight: 800, color: '#ff3269', textAlign: 'center', marginBottom: '8px' }}>⏳ 3 days remaining!</div>

                      {modalTab === 'walkthrough' && (
                        <div style={{ display: 'flex', flexDirection: 'column', flex: 1, justifyContent: 'space-between' }}>
                          {walkthroughSlide === 1 && (
                            <div>
                              <div style={{ fontSize: '0.72rem', fontWeight: 800, color: '#334155', marginBottom: '8px' }}>How it works</div>
                              <div className="step-card"><div className="step-icon-wrap step-icon-1">🛍️</div><div><strong style={{fontSize:'0.72rem'}}>STEP 1: Buy Products</strong><br/><span style={{fontSize:'0.62rem', color:'#64748b'}}>Select products with the Hunt badge to get started.</span></div></div>
                              <div className="step-card"><div className="step-icon-wrap step-icon-2">🗝️</div><div><strong style={{fontSize:'0.72rem'}}>STEP 2: Unlock Clues</strong><br/><span style={{fontSize:'0.62rem', color:'#64748b'}}>Every purchase unlocks a mystery clue in your Hunt dashboard.</span></div></div>
                              <div className="step-card"><div className="step-icon-wrap step-icon-3">🔍</div><div><strong style={{fontSize:'0.72rem'}}>STEP 3: Find the Item</strong><br/><span style={{fontSize:'0.62rem', color:'#64748b'}}>Use your clues to solve the puzzle and locate the secret item.</span></div></div>
                              <div className="step-card"><div className="step-icon-wrap step-icon-4">🏷️</div><div><strong style={{fontSize:'0.72rem'}}>STEP 4: Get Discount</strong><br/><span style={{fontSize:'0.62rem', color:'#64748b'}}>Add the secret item to your cart and watch the price drop!</span></div></div>
                            </div>
                          )}

                          {walkthroughSlide === 2 && (
                            <div>
                              <div className="level-progress-bar">
                                <div className="level-badge done">✓</div>
                                <div className="level-badge done">✓</div>
                                <div className="level-badge current">3</div>
                                <div className="level-badge">🔒</div>
                              </div>
                              <div style={{ fontSize: '0.58rem', fontWeight: 900, color: '#16a34a', textAlign: 'center', marginBottom: '2px' }}>LEVEL 3: THE GHOST IN THE LIVING ROOM</div>
                              <div style={{ fontSize: '0.82rem', fontWeight: 900, textAlign: 'center', marginBottom: '10px' }}>Current Challenge</div>

                              <div className="clue-box">
                                <p className="clue-riddle">"I test friendships, press your buttons, and turn grown adults into yelling kids at 2 AM. I live right next to your TV. What am I?"</p>
                                <div className="hint-pill-btn" style={{ display: 'inline-block' }}>Hint: Check Gaming</div>
                              </div>
                            </div>
                          )}

                          {walkthroughSlide === 3 && (
                            <div className="reward-card-purple">
                              <div style={{ fontSize: '1.8rem' }}>🎖️</div>
                              <div style={{ fontSize: '1.15rem', fontWeight: 900, margin: '4px 0' }}>Prize: ₹50 OFF</div>
                              <p style={{ fontSize: '0.68rem', opacity: 0.9, marginBottom: '10px' }}>Unlock this mystery coupon for your next cart!</p>
                              <button className="unlock-now-btn" onClick={() => setModalTab('rewards')}>⚡ Check My Rewards</button>
                              <div style={{ fontSize: '0.55rem', opacity: 0.7, marginTop: '6px' }}>Valid for next 12 hours only</div>
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
                            <div className="level-progress-bar">
                              <div className="level-badge done">✓</div>
                              <div className="level-badge done">✓</div>
                              <div className="level-badge current">3</div>
                              <div className="level-badge">🔒</div>
                            </div>
                            <div style={{ fontSize: '0.62rem', fontWeight: 900, color: '#16a34a', textAlign: 'center', marginBottom: '6px' }}>MY UNLOCKED CLUES</div>

                            <div style={{ background: '#f8fafc', border: '1px solid #e2e8f0', borderRadius: '8px', padding: '6px 10px', marginBottom: '6px' }}>
                              <div style={{ fontSize: '0.58rem', fontWeight: 900, color: '#16a34a' }}>✓ LEVEL 1 CLUE UNLOCKED</div>
                              <div style={{ fontSize: '0.65rem', fontStyle: 'italic', color: '#334155' }}>"Looking for crunch? Check snack aisles..."</div>
                            </div>

                            <div style={{ background: '#f8fafc', border: '1px solid #e2e8f0', borderRadius: '8px', padding: '6px 10px', marginBottom: '6px' }}>
                              <div style={{ fontSize: '0.58rem', fontWeight: 900, color: '#16a34a' }}>✓ LEVEL 2 CLUE UNLOCKED</div>
                              <div style={{ fontSize: '0.65rem', fontStyle: 'italic', color: '#334155' }}>"Need fresh greens? Check fruits & veg..."</div>
                            </div>

                            <div className="clue-box" style={{ margin: '4px 0 0 0', padding: '8px 10px' }}>
                              <div style={{ fontSize: '0.55rem', fontWeight: 900, color: '#c2410c', marginBottom: '2px' }}>🎯 LEVEL 3 ACTIVE CHALLENGE</div>
                              <p className="clue-riddle" style={{ fontSize: '0.68rem', margin: '3px 0' }}>"I test friendships, press your buttons, and turn grown adults into yelling kids at 2 AM. I live right next to your TV. What am I?"</p>
                              <div className="hint-pill-btn" style={{ display: 'inline-block', fontSize: '0.58rem', padding: '2px 8px' }}>Hint: Check Gaming</div>
                            </div>
                          </div>
                        </div>
                      )}

                      {modalTab === 'rewards' && (
                        <div style={{ display: 'flex', flexDirection: 'column', flex: 1, justifyContent: 'space-between' }}>
                          {(huntUnlocked || (selectedProduct && selectedProduct.isHuntItem && cartCount > 0)) ? (
                            <div className="reward-card-purple" style={{ background: 'linear-gradient(135deg, #0c831f, #10b981)', padding: '16px' }}>
                              <div style={{ fontSize: '1.8rem' }}>🎉 🎖️</div>
                              <div style={{ fontSize: '1.1rem', fontWeight: 900, margin: '4px 0' }}>Prize: ₹50 OFF UNLOCKED!</div>
                              <div style={{ background: 'white', color: '#0c831f', padding: '5px 12px', borderRadius: '8px', fontWeight: 900, fontSize: '0.8rem', display: 'inline-block', margin: '8px 0' }}>
                                COUPON CODE: ACCZ50OFF
                              </div>
                              <p style={{ fontSize: '0.68rem', opacity: 0.95, margin: '4px 0' }}>Congratulations! Coupon is auto-applied to your checkout order.</p>
                              <button className="unlock-now-btn" style={{ color: '#0c831f', marginTop: '10px' }} onClick={() => { setShowModal(false); setScreen('cart'); }}>⚡ View Cart & Pay</button>
                            </div>
                          ) : (
                            <div style={{ background: '#f8fafc', border: '1.5px dashed #cbd5e1', borderRadius: '16px', padding: '16px', textAlign: 'center', color: '#64748b' }}>
                              <div style={{ fontSize: '1.8rem' }}>🔒</div>
                              <div style={{ fontSize: '1.05rem', fontWeight: 900, color: '#334155', margin: '4px 0' }}>Prize: ₹50 OFF</div>
                              <div style={{ background: '#e2e8f0', color: '#64748b', padding: '5px 12px', borderRadius: '8px', fontWeight: 800, fontSize: '0.78rem', display: 'inline-block', margin: '8px 0', filter: 'blur(3px)', userSelect: 'none' }}>
                                COUPON: ACCZ50OFF
                              </div>
                              <p style={{ fontSize: '0.68rem', color: '#64748b', margin: '6px 0' }}>Add the secret Hunt product (Gamepad) to your cart to unlock this coupon!</p>
                              <button disabled style={{ background: '#e2e8f0', color: '#94a3b8', border: 'none', width: '100%', padding: '8px', borderRadius: '10px', fontSize: '0.78rem', fontWeight: 800, marginTop: '10px', cursor: 'not-allowed' }}>
                                🔒 Locked (Find Hunt Item to Unlock)
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

final_html = raw_html_template.replace("__DEMO_MODE__", st.session_state.demo_mode)
components.html(final_html, height=650, scrolling=False)
