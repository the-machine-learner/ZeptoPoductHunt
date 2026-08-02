import React, { useState } from 'react';
import { X, Check, Lock, Gift, ShoppingCart, Sparkles, ChevronRight, HelpCircle } from 'lucide-react';

export function HuntModal({ onClose, onNavigateToCategory, cartCount, modalTab, setModalTab, tutorialStep }) {
  return (
    <div className="modal-overlay">
      <div className="modal-bottom-sheet">
        {/* Close Button */}
        <div className="modal-close-btn" onClick={onClose}>
          <X size={18} />
        </div>

        {/* Modal Title */}
        <div className="modal-header-title">PRODUCT HUNT WEEK</div>

        {/* TAB 1: WALKTHROUGH (Screen 2) */}
        {modalTab === 'walkthrough' && (
          <div id="modal-tab-walkthrough-content">
            <div style={{ fontSize: '0.85rem', fontWeight: 800, color: '#334155', marginBottom: '12px' }}>
              How it works
            </div>

            <div className="step-card">
              <div className="step-icon-wrap step-icon-1">🛍️</div>
              <div className="step-text-wrap">
                <span className="step-num">STEP 1</span>
                <span className="step-title">Buy Products</span>
                <span className="step-desc">Select products with the Hunt badge to get started.</span>
              </div>
            </div>

            <div className="step-card">
              <div className="step-icon-wrap step-icon-2">🗝️</div>
              <div className="step-text-wrap">
                <span className="step-num">STEP 2</span>
                <span className="step-title">Unlock Clues</span>
                <span className="step-desc">Every purchase unlocks a mystery clue in your Hunt dashboard.</span>
              </div>
            </div>

            <div className="step-card">
              <div className="step-icon-wrap step-icon-3">🔍</div>
              <div className="step-text-wrap">
                <span className="step-num">STEP 3</span>
                <span className="step-title">Find the Item</span>
                <span className="step-desc">Use your clues to solve the puzzle and locate the secret item.</span>
              </div>
            </div>

            <div className="step-card">
              <div className="step-icon-wrap step-icon-4">🏷️</div>
              <div className="step-text-wrap">
                <span className="step-num">STEP 4</span>
                <span className="step-title">Get Discount</span>
                <span className="step-desc">Add the secret item to your cart and watch the price drop!</span>
              </div>
            </div>
          </div>
        )}

        {/* TAB 2: CLUES / CURRENT CHALLENGE (Screen 3) */}
        {modalTab === 'clues' && (
          <div id="modal-tab-clues-content">
            {/* Level Milestone Icons */}
            <div className="level-progress-bar">
              <div className="level-badge done"><Check size={14} /></div>
              <div className="level-badge done"><Check size={14} /></div>
              <div className="level-badge current">3</div>
              <div className="level-badge"><Lock size={12} /></div>
            </div>

            <div style={{ textTransform: 'uppercase', fontSize: '0.68rem', fontWeight: 900, color: '#16a34a', textAlign: 'center' }}>
              LEVEL 3: THE GHOST IN THE LIVING ROOM
            </div>
            <div style={{ fontSize: '1rem', fontWeight: 900, textAlign: 'center', color: '#1e293b', margin: '2px 0 14px 0' }}>
              Current Challenge
            </div>

            {/* Riddle Box */}
            <div className="clue-box" id="clue-box-target">
              <p className="clue-riddle">
                "I test friendships, press your buttons, and turn grown adults into yelling kids at 2 AM. I live right next to your TV. What am I?"
              </p>
              <button
                className="hint-pill-btn"
                onClick={() => onNavigateToCategory('Electronics')}
              >
                Hint: Check Gaming →
              </button>
            </div>
          </div>
        )}

        {/* TAB 3: REWARDS (Screen 4) */}
        {modalTab === 'rewards' && (
          <div id="modal-tab-rewards-content">
            <div className="reward-card-purple" id="reward-card-target">
              <div style={{ fontSize: '2.5rem' }}>🏆</div>
              <div className="prize-title">Prize: ₹50 OFF</div>
              <p style={{ fontSize: '0.8rem', opacity: 0.9 }}>
                Unlock this mystery coupon for your next cart!
              </p>
              <button
                className="unlock-now-btn"
                onClick={() => onNavigateToCategory('Electronics')}
              >
                ⚡ Unlock Now
              </button>
              <div style={{ fontSize: '0.68rem', opacity: 0.75, marginTop: '8px' }}>
                Valid for next 12 hours only
              </div>
            </div>
          </div>
        )}

        {/* Pagination Dots */}
        <div className="pagination-dots">
          <span className={modalTab === 'walkthrough' ? 'active' : ''} onClick={() => setModalTab('walkthrough')} />
          <span className={modalTab === 'clues' ? 'active' : ''} onClick={() => setModalTab('clues')} />
          <span className={modalTab === 'rewards' ? 'active' : ''} onClick={() => setModalTab('rewards')} />
        </div>

        {/* Modal Navigation Tabs */}
        <div className="modal-nav-bar" id="modal-tab-nav-bar">
          <div
            id="modal-tab-walkthrough"
            className={`modal-nav-tab ${modalTab === 'walkthrough' ? 'active' : ''}`}
            onClick={() => setModalTab('walkthrough')}
          >
            Walkthrough
          </div>
          <div
            id="modal-tab-clues"
            className={`modal-nav-tab ${modalTab === 'clues' ? 'active' : ''}`}
            onClick={() => setModalTab('clues')}
          >
            Clues
          </div>
          <div
            id="modal-tab-rewards"
            className={`modal-nav-tab ${modalTab === 'rewards' ? 'active' : ''}`}
            onClick={() => setModalTab('rewards')}
          >
            Rewards
          </div>
        </div>
      </div>
    </div>
  );
}
