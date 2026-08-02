import React from 'react';
import { Search, MapPin, Zap, ShoppingBag, Grid, RotateCcw, Printer, Flame, Sparkles } from 'lucide-react';

export function HomeScreen({
  onOpenHunt,
  onSelectCategory,
  onNavigateToCart,
  cartCount,
  activeTab,
  setActiveTab,
  tutorialStep
}) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', flex: 1 }}>
      {/* Header */}
      <div className="home-header">
        <div className="location-bar">
          <div>
            <div style={{ fontSize: '0.65rem', textTransform: 'uppercase', opacity: 0.85, fontWeight: 700 }}>
              DELIVERING TO
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
              <span className="address-text">Flat - 803, Ruby, Gulmohar Orch...</span>
              <span style={{ fontSize: '0.7rem' }}>▼</span>
            </div>
          </div>
          <div className="eta-pill">
            <Zap size={14} fill="currentColor" />
            6 minutes
          </div>
        </div>

        {/* Search Bar */}
        <div className="search-box-wrap">
          <Search className="search-icon" size={18} />
          <input
            type="text"
            className="search-input"
            placeholder='Search for "Face Wash"'
            readOnly
            onClick={() => onSelectCategory('Electronics')}
          />
          <div className="pet-store-chip">
            <span>🐶</span> Pet Store
          </div>
        </div>

        {/* Category Scroll Chips */}
        <div className="category-chips-scroll">
          <div className="cat-chip active">All</div>
          <div className="cat-chip">It's Raining</div>
          <div className="cat-chip">Pooja</div>
          <div className="cat-chip">Fresh</div>
          <div className="cat-chip">Toys</div>
          <div
            id="cat-chip-electronics"
            className={`cat-chip ${tutorialStep === 5 ? 'highlight-box' : ''}`}
            onClick={() => onSelectCategory('Electronics')}
          >
            ⚡ Electronics
          </div>
          <div className="cat-chip">Fashion</div>
        </div>
      </div>

      {/* Main Home Content */}
      <div className="home-content-body">
        {/* Banner Card */}
        <div
          className="floating-hunt-banner"
          id="banner-hunt-trigger"
          onClick={onOpenHunt}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <div style={{ fontSize: '1.6rem' }}>🎯</div>
            <div>
              <div style={{ fontSize: '0.75rem', fontWeight: 800, textTransform: 'uppercase', opacity: 0.9 }}>
                LIMITED TIME EVENT
              </div>
              <div style={{ fontSize: '0.95rem', fontWeight: 900 }}>PRODUCT HUNT WEEK</div>
            </div>
          </div>
          <button
            style={{
              background: 'white',
              color: '#ff3269',
              border: 'none',
              padding: '6px 12px',
              borderRadius: '20px',
              fontWeight: 800,
              fontSize: '0.75rem'
            }}
          >
            PLAY NOW →
          </button>
        </div>

        {/* Categories Grid */}
        <div style={{ fontSize: '0.85rem', fontWeight: 800, color: '#334155', marginTop: '4px' }}>
          Explore Categories
        </div>
        <div className="category-grid">
          <div className="cat-card" onClick={() => onSelectCategory('Essentials')}>
            <div className="cat-card-img" style={{ background: '#fef3c7', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '1.3rem' }}>
              🥦
            </div>
            <div className="cat-card-title">Cooking Essentials</div>
            <div className="cat-card-off">UPTO 70% OFF</div>
          </div>

          <div className="cat-card" onClick={() => onSelectCategory('Personal')}>
            <div className="cat-card-img" style={{ background: '#fce7f3', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '1.3rem' }}>
              🧴
            </div>
            <div className="cat-card-title">Personal Care</div>
            <div className="cat-card-off">UPTO 85% OFF</div>
          </div>

          <div className="cat-card" onClick={() => onSelectCategory('Cleaning')}>
            <div className="cat-card-img" style={{ background: '#e0f2fe', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '1.3rem' }}>
              🧼
            </div>
            <div className="cat-card-title">Cleaning Essentials</div>
            <div className="cat-card-off">UPTO 80% OFF</div>
          </div>

          <div className="cat-card" onClick={() => onSelectCategory('Breakfast')}>
            <div className="cat-card-img" style={{ background: '#ffedd5', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '1.3rem' }}>
              🥣
            </div>
            <div className="cat-card-title">Breakfast & Instant</div>
            <div className="cat-card-off">UPTO 50% OFF</div>
          </div>

          <div className="cat-card" onClick={() => onSelectCategory('Fitness')}>
            <div className="cat-card-img" style={{ background: '#dcfce7', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '1.3rem' }}>
              🏋️
            </div>
            <div className="cat-card-title">Protein & Fitness</div>
            <div className="cat-card-off">UPTO 45% OFF</div>
          </div>

          <div
            className="cat-card"
            id="cat-card-gaming"
            onClick={() => onSelectCategory('Electronics')}
          >
            <div className="cat-card-img" style={{ background: '#e0e7ff', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '1.3rem' }}>
              🎮
            </div>
            <div className="cat-card-title">Electronics & Gaming</div>
            <div className="cat-card-off" style={{ background: '#e0e7ff', color: '#4338ca' }}>
              HUNT ITEM
            </div>
          </div>
        </div>

        {/* Steal Deals */}
        <div className="steal-deals-banner">
          <div>
            <div style={{ fontSize: '0.7rem', fontWeight: 800, color: '#fbbf24', textTransform: 'uppercase' }}>
              OFFERS & DISCOUNTS
            </div>
            <div style={{ fontSize: '0.95rem', fontWeight: 800, marginTop: '2px' }}>
              Unlock extra ₹50 OFF
            </div>
            <div style={{ fontSize: '0.72rem', opacity: 0.8, marginTop: '2px' }}>
              Shop for ₹241 more
            </div>
          </div>
          <div style={{ background: '#ff3269', color: 'white', width: '36px', height: '36px', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 900, fontSize: '0.9rem' }}>
            %
          </div>
        </div>
      </div>

      {/* Bottom Nav Bar */}
      <div className="bottom-nav-bar">
        <div className="nav-item active">
          <ShoppingBag size={20} />
          <span>Home</span>
        </div>
        <div className="nav-item" onClick={() => onSelectCategory('Electronics')}>
          <Grid size={20} />
          <span>Categories</span>
        </div>
        <div className="nav-item">
          <RotateCcw size={20} />
          <span>Buy Again</span>
        </div>
        <div className="nav-item">
          <Printer size={20} />
          <span>Print</span>
        </div>
        <div
          id="nav-hunt-btn"
          className="nav-item hunt-highlight"
          onClick={onOpenHunt}
        >
          <span className="hunt-badge">EVENT</span>
          <Flame size={22} color="#ff3269" />
          <span>Hunt</span>
        </div>
      </div>
    </div>
  );
}
