import React from 'react';
import { ArrowLeft, Search, Mic, Sparkles, Gamepad2, Headphones, Tv, Smartphone, Watch, Lightbulb } from 'lucide-react';

export function CategoryScreen({ onBack, onSelectProduct, tutorialStep }) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', flex: 1, background: '#f8fafc' }}>
      {/* Category Header */}
      <div style={{ background: 'white', padding: '12px 16px', borderBottom: '1px solid #e2e8f0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '10px' }}>
          <ArrowLeft size={20} style={{ cursor: 'pointer' }} onClick={onBack} />
          <div className="search-box-wrap" style={{ flex: 1, marginBottom: 0 }}>
            <Search className="search-icon" size={18} />
            <input
              type="text"
              className="search-input"
              value='Gaming & Electronics'
              readOnly
              style={{ background: '#f1f5f9' }}
            />
            <div className="pet-store-chip" style={{ background: '#e0e7ff', color: '#4338ca' }}>
              Pet Store
            </div>
          </div>
        </div>

        {/* Top Category Chips */}
        <div className="category-chips-scroll">
          <div className="cat-chip" style={{ background: '#f1f5f9', color: '#475569' }}>Fresh</div>
          <div className="cat-chip" style={{ background: '#f1f5f9', color: '#475569' }}>Toys</div>
          <div className="cat-chip active" style={{ background: '#0c831f', color: 'white' }}>Electronics</div>
          <div className="cat-chip" style={{ background: '#f1f5f9', color: '#475569' }}>Fashion</div>
          <div className="cat-chip" style={{ background: '#f1f5f9', color: '#475569' }}>Mobiles</div>
        </div>
      </div>

      {/* Main Subcategories Grid */}
      <div style={{ padding: '14px', flex: 1 }}>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '12px', marginBottom: '16px' }}>
          <div style={{ textAlignment: 'center', textAlign: 'center' }}>
            <div style={{ background: '#f1f5f9', borderRadius: '16px', padding: '12px', marginBottom: '4px', fontSize: '1.4rem' }}>🎧</div>
            <div style={{ fontSize: '0.65rem', fontWeight: 700, color: '#475569' }}>Audio Store</div>
          </div>

          <div style={{ textAlignment: 'center', textAlign: 'center' }}>
            <div style={{ background: '#f1f5f9', borderRadius: '16px', padding: '12px', marginBottom: '4px', fontSize: '1.4rem' }}>🍳</div>
            <div style={{ fontSize: '0.65rem', fontWeight: 700, color: '#475569' }}>Kitchen</div>
          </div>

          <div style={{ textAlignment: 'center', textAlign: 'center' }}>
            <div style={{ background: '#f1f5f9', borderRadius: '16px', padding: '12px', marginBottom: '4px', fontSize: '1.4rem' }}>📺</div>
            <div style={{ fontSize: '0.65rem', fontWeight: 700, color: '#475569' }}>Appliances</div>
          </div>

          <div style={{ textAlignment: 'center', textAlign: 'center' }}>
            <div style={{ background: '#f1f5f9', borderRadius: '16px', padding: '12px', marginBottom: '4px', fontSize: '1.4rem' }}>🧴</div>
            <div style={{ fontSize: '0.65rem', fontWeight: 700, color: '#475569' }}>Personal Care</div>
          </div>

          <div style={{ textAlignment: 'center', textAlign: 'center' }}>
            <div style={{ background: '#f1f5f9', borderRadius: '16px', padding: '12px', marginBottom: '4px', fontSize: '1.4rem' }}>📱</div>
            <div style={{ fontSize: '0.65rem', fontWeight: 700, color: '#475569' }}>Mobiles</div>
          </div>

          <div
            id="subcategory-gaming"
            style={{
              textAlign: 'center',
              cursor: 'pointer',
              border: tutorialStep === 6 ? '2px solid #ff3269' : 'none',
              borderRadius: '16px',
              padding: '2px'
            }}
            onClick={onSelectProduct}
          >
            <div style={{ background: '#e0e7ff', color: '#4338ca', borderRadius: '16px', padding: '12px', marginBottom: '4px', fontSize: '1.4rem' }}>
              🎮
            </div>
            <div style={{ fontSize: '0.65rem', fontWeight: 800, color: '#4338ca' }}>Gaming & Ent.</div>
          </div>

          <div style={{ textAlignment: 'center', textAlign: 'center' }}>
            <div style={{ background: '#f1f5f9', borderRadius: '16px', padding: '12px', marginBottom: '4px', fontSize: '1.4rem' }}>🔌</div>
            <div style={{ fontSize: '0.65rem', fontWeight: 700, color: '#475569' }}>Tech Acc.</div>
          </div>

          <div style={{ textAlignment: 'center', textAlign: 'center' }}>
            <div style={{ background: '#f1f5f9', borderRadius: '16px', padding: '12px', marginBottom: '4px', fontSize: '1.4rem' }}>💡</div>
            <div style={{ fontSize: '0.65rem', fontWeight: 700, color: '#475569' }}>Lighting</div>
          </div>
        </div>

        {/* Promo Card */}
        <div style={{ background: '#eff6ff', border: '1px solid #bfdbfe', borderRadius: '12px', padding: '10px 12px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '16px' }}>
          <div style={{ fontSize: '0.72rem', color: '#1e40af', fontWeight: 700 }}>
            Flat 5% off up to ₹1500 with HSBC Credit Cards
          </div>
          <span style={{ fontSize: '0.7rem', fontWeight: 800, color: '#1d4ed8' }}>T&C</span>
        </div>

        {/* Trending Deals Section */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
          <div style={{ fontSize: '0.9rem', fontWeight: 900, color: '#1e293b' }}>Trending deals</div>
          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#0c831f' }}>See All &gt;</span>
        </div>

        {/* Target Product Card */}
        <div
          id="product-card-gamepad"
          style={{
            background: 'white',
            borderRadius: '18px',
            padding: '14px',
            boxShadow: '0 4px 12px rgba(0, 0, 0, 0.05)',
            display: 'flex',
            gap: '14px',
            alignItems: 'center',
            cursor: 'pointer',
            border: tutorialStep === 6 ? '2px solid #ff3269' : '1px solid #e2e8f0'
          }}
          onClick={onSelectProduct}
        >
          <div style={{ background: '#0f172a', borderRadius: '14px', padding: '10px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <span style={{ fontSize: '2.5rem' }}>🎮</span>
          </div>
          <div style={{ flex: 1 }}>
            <div style={{ background: '#ffedd5', color: '#c2410c', fontSize: '0.62rem', fontWeight: 800, padding: '2px 6px', borderRadius: '6px', display: 'inline-block', marginBottom: '4px' }}>
              🎯 HUNT ITEM DETECTED
            </div>
            <div style={{ fontSize: '0.82rem', fontWeight: 800, color: '#1e293b', lineHeight: 1.2, marginBottom: '6px' }}>
              Zebronics MAX FURY Transparent RGB LED Wired Gamepad
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{ fontSize: '0.95rem', fontWeight: 900, color: '#1e293b' }}>₹1080</span>
              <span style={{ fontSize: '0.72rem', textDecoration: 'line-through', color: '#94a3b8' }}>₹1999</span>
              <span style={{ fontSize: '0.7rem', fontWeight: 800, color: '#10b981', background: '#e6f4ea', padding: '2px 6px', borderRadius: '6px' }}>
                45% OFF
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
