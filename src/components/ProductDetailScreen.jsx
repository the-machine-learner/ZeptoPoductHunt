import React from 'react';
import { ArrowLeft, Search, Share2, Heart, Zap, ShoppingBag } from 'lucide-react';

export function ProductDetailScreen({ onBack, onAddToCart, tutorialStep }) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', flex: 1, background: '#f8fafc', position: 'relative', paddingBottom: '70px' }}>
      {/* Top Navbar */}
      <div style={{ background: 'white', padding: '12px 16px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid #e2e8f0' }}>
        <ArrowLeft size={20} style={{ cursor: 'pointer' }} onClick={onBack} />
        <div style={{ display: 'flex', gap: '16px', color: '#475569' }}>
          <Search size={20} />
          <Share2 size={20} />
          <Heart size={20} />
        </div>
      </div>

      {/* Main PDP Image */}
      <div className="pdp-image-box">
        <div style={{ background: '#0f172a', borderRadius: '24px', padding: '30px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <span style={{ fontSize: '5rem' }}>🎮</span>
        </div>
        <div className="rating-badge">
          4.2 ★ <span>581</span>
        </div>
      </div>

      {/* Product Information */}
      <div className="pdp-info-card">
        {/* Badges */}
        <div style={{ display: 'flex', gap: '6px', marginBottom: '8px' }}>
          <span style={{ background: '#f1f5f9', color: '#475569', fontSize: '0.65rem', fontWeight: 800, padding: '2px 8px', borderRadius: '6px' }}>
            Open Box Verification
          </span>
          <span style={{ background: '#e0e7ff', color: '#4338ca', fontSize: '0.65rem', fontWeight: 800, padding: '2px 8px', borderRadius: '6px' }}>
            RGB LED Gamepad
          </span>
        </div>

        <h1 className="pdp-title">
          Zebronics MAX FURY Transparent RGB LED Wired Gamepad | Dual Analog Sticks | Quad Triggers | Dual Motor Force Feedback | Haptic Feedback | Compatible With Windows PC & Android | Black
        </h1>

        <div style={{ fontSize: '0.72rem', color: '#64748b', marginBottom: '6px' }}>
          Net Qty: <span style={{ fontWeight: 700, color: '#1e293b' }}>1 pc</span>
        </div>

        {/* Pricing */}
        <div className="pdp-price-row">
          <span className="price-main">₹1080</span>
          <span style={{ fontSize: '0.8rem', textDecoration: 'line-through', color: '#94a3b8' }}>₹1999</span>
          <span className="price-off">45% OFF</span>
        </div>
        <div style={{ fontSize: '0.68rem', color: '#94a3b8', marginTop: '2px' }}>
          (incl. of all taxes)
        </div>

        {/* ETA */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '6px', marginTop: '12px', background: '#e6f4ea', color: '#0c831f', padding: '8px 12px', borderRadius: '10px', fontSize: '0.78rem', fontWeight: 800 }}>
          <Zap size={16} fill="currentColor" />
          ⚡ Delivering in 22 mins
        </div>
      </div>

      {/* Sticky Bottom Bar */}
      <div className="sticky-bottom-add">
        <div style={{ background: '#f1f5f9', padding: '10px', borderRadius: '12px', color: '#475569' }}>
          <ShoppingBag size={22} />
        </div>
        <button
          id="btn-add-to-cart-pdp"
          className="btn-add-cart-pink"
          onClick={onAddToCart}
        >
          Add to Cart
        </button>
      </div>
    </div>
  );
}
