import React, { useState, useEffect } from 'react';
import { HomeScreen } from './components/HomeScreen';
import { HuntModal } from './components/HuntModal';
import { CategoryScreen } from './components/CategoryScreen';
import { ProductDetailScreen } from './components/ProductDetailScreen';
import { CartScreen } from './components/CartScreen';
import { GuidedTutorialOverlay } from './components/GuidedTutorialOverlay';
import { RotateCcw, Smartphone, Play, CheckCircle } from 'lucide-react';

export default function App() {
  const [screen, setScreen] = useState('home'); // 'home' | 'category' | 'pdp' | 'cart'
  const [showModal, setShowModal] = useState(false);
  const [modalTab, setModalTab] = useState('walkthrough'); // 'walkthrough' | 'clues' | 'rewards'
  const [cartCount, setCartCount] = useState(0);
  const [tutorialStep, setTutorialStep] = useState(1); // 1 to 8, 0 = off
  const [targetRect, setTargetRect] = useState(null);

  // Trigger Guided Tutorial Step rect measurements
  useEffect(() => {
    if (tutorialStep <= 0) {
      setTargetRect(null);
      return;
    }

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
        setTargetRect({
          top: rect.top,
          left: rect.left,
          width: rect.width,
          height: rect.height,
        });
      } else {
        setTargetRect(null);
      }
    };

    const timer = setTimeout(updateRect, 300);
    window.addEventListener('resize', updateRect);
    return () => {
      clearTimeout(timer);
      window.removeEventListener('resize', updateRect);
    };
  }, [tutorialStep, screen, showModal, modalTab]);

  // Handle Confetti
  const triggerConfetti = () => {
    if (window.confetti) {
      window.confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 }
      });
    }
  };

  // Guided Tutorial Step Data
  const getTutorialStepData = () => {
    switch (tutorialStep) {
      case 1:
        return {
          title: "Step 1: Open Product Hunt",
          description: "Tap the highlighted 'Hunt' icon at the bottom right to enter Product Hunt Week!",
          buttonText: "Open Hunt Modal →",
          targetRect,
          tooltipBottom: 80,
          onAction: () => {
            setShowModal(true);
            setModalTab('walkthrough');
            setTutorialStep(2);
          }
        };
      case 2:
        return {
          title: "Step 2: Walkthrough (How It Works)",
          description: "Review the 4-step game rules: Buy Products → Unlock Clues → Find Item → Get Discount!",
          buttonText: "View Clue →",
          targetRect,
          tooltipBottom: 160,
          onAction: () => {
            setModalTab('clues');
            setTutorialStep(3);
          }
        };
      case 3:
        return {
          title: "Step 3: Read Your Spicy AI Clue",
          description: "Level 3 Challenge: 'I test friendships, press your buttons... I live right next to your TV.' Hint: Gaming!",
          buttonText: "Check Rewards →",
          targetRect,
          tooltipBottom: 160,
          onAction: () => {
            setModalTab('rewards');
            setTutorialStep(4);
          }
        };
      case 4:
        return {
          title: "Step 4: Check Unlocking Prize",
          description: "Prize: ₹50 OFF Coupon code for your cart when you find & add the secret item!",
          buttonText: "Go Hunt Item →",
          targetRect,
          tooltipBottom: 160,
          onAction: () => {
            setShowModal(false);
            setScreen('category');
            setTutorialStep(6);
          }
        };
      case 5:
        return {
          title: "Step 5: Browse Category",
          description: "Navigate to Electronics & Gaming where the clue item is located.",
          buttonText: "Go to Gaming →",
          targetRect,
          tooltipTop: 160,
          onAction: () => {
            setScreen('category');
            setTutorialStep(6);
          }
        };
      case 6:
        return {
          title: "Step 6: Select Secret Product",
          description: "Found it! Tap on the Zebronics MAX FURY RGB Gamepad (Hunt Item Detected).",
          buttonText: "Open Item →",
          targetRect,
          tooltipBottom: 80,
          onAction: () => {
            setScreen('pdp');
            setTutorialStep(7);
          }
        };
      case 7:
        return {
          title: "Step 7: Add to Cart",
          description: "Tap 'Add to Cart' to trigger the Flash Sale price and unlock your coupon code!",
          buttonText: "Add to Cart →",
          targetRect,
          tooltipBottom: 80,
          onAction: () => {
            setCartCount(1);
            setScreen('cart');
            setTutorialStep(8);
            triggerConfetti();
          }
        };
      case 8:
        return {
          title: "Step 8: Coupon ACCZ50OFF Unlocked! 🎉",
          description: "Boom! Level 3 complete. COUPON CODE: ACCZ50OFF is unlocked & applied to your cart!",
          buttonText: "Finish Tour 🚀",
          targetRect,
          tooltipTop: 100,
          onAction: () => {
            setTutorialStep(0);
          }
        };
      default:
        return null;
    }
  };

  const currentStepData = getTutorialStepData();

  const handleTutorialNext = () => {
    if (currentStepData && currentStepData.onAction) {
      currentStepData.onAction();
    } else {
      setTutorialStep(prev => (prev < 8 ? prev + 1 : 0));
    }
  };

  const handleTutorialPrev = () => {
    setTutorialStep(prev => Math.max(1, prev - 1));
  };

  const handleTutorialSkip = () => {
    setTutorialStep(0);
  };

  const handleRestartTour = () => {
    setScreen('home');
    setShowModal(false);
    setModalTab('walkthrough');
    setCartCount(0);
    setTutorialStep(1);
  };

  const handleOpenHunt = () => {
    setShowModal(true);
    setModalTab('walkthrough');
    if (tutorialStep === 1) setTutorialStep(2);
  };

  const handleNavigateToCategory = (catName) => {
    setShowModal(false);
    setScreen('category');
    if (tutorialStep >= 2 && tutorialStep <= 5) setTutorialStep(6);
  };

  const handleSelectProduct = () => {
    setScreen('pdp');
    if (tutorialStep === 6) setTutorialStep(7);
  };

  const handleAddToCart = () => {
    setCartCount(1);
    setScreen('cart');
    triggerConfetti();
    if (tutorialStep === 7) setTutorialStep(8);
  };

  return (
    <div className="app-viewport-container">
      {/* Desktop Controls Header */}
      <header className="control-header">
        <div className="control-title">
          <span>Zepto</span> Product Hunt MVP
        </div>
        <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
          <button className="btn-tour-restart" onClick={handleRestartTour}>
            <Play size={14} fill="currentColor" /> Restart Guided Tour
          </button>
        </div>
      </header>

      {/* Mobile Device Container */}
      <div className="mobile-device-frame">
        {/* Top Status Bar */}
        <div className="status-bar">
          <div className="status-time">11:08</div>
          <div className="phone-notch" />
          <div className="status-icons">
            <span>5G</span>
            <span>⚡ 6m</span>
            <span>🔋</span>
          </div>
        </div>

        {/* Mobile Viewport Body */}
        <div className="mobile-screen-body">
          {screen === 'home' && (
            <HomeScreen
              onOpenHunt={handleOpenHunt}
              onSelectCategory={handleNavigateToCategory}
              onNavigateToCart={() => setScreen('cart')}
              cartCount={cartCount}
              activeTab="home"
              setActiveTab={() => {}}
              tutorialStep={tutorialStep}
            />
          )}

          {screen === 'category' && (
            <CategoryScreen
              onBack={() => setScreen('home')}
              onSelectProduct={handleSelectProduct}
              tutorialStep={tutorialStep}
            />
          )}

          {screen === 'pdp' && (
            <ProductDetailScreen
              onBack={() => setScreen('category')}
              onAddToCart={handleAddToCart}
              tutorialStep={tutorialStep}
            />
          )}

          {screen === 'cart' && (
            <CartScreen
              onBack={() => setScreen('pdp')}
              onResetDemo={handleRestartTour}
            />
          )}

          {/* Product Hunt Modal Bottom Sheet */}
          {showModal && (
            <HuntModal
              onClose={() => setShowModal(false)}
              onNavigateToCategory={handleNavigateToCategory}
              cartCount={cartCount}
              modalTab={modalTab}
              setModalTab={setModalTab}
              tutorialStep={tutorialStep}
            />
          )}

          {/* Interactive Guided Overlay */}
          {tutorialStep > 0 && (
            <GuidedTutorialOverlay
              currentStep={tutorialStep}
              totalSteps={8}
              stepData={currentStepData}
              onNext={handleTutorialNext}
              onPrev={handleTutorialPrev}
              onSkip={handleTutorialSkip}
            />
          )}
        </div>
      </div>
    </div>
  );
}
