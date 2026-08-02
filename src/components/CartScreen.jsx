import React from 'react';
import { ArrowLeft, Check, Sparkles, Clock, ShieldCheck, Ticket } from 'lucide-react';

export function CartScreen({ onBack, onResetDemo }) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', flex: 1, background: '#f8fafc', position: 'relative', paddingBottom: '70px' }}>
      {/* Cart Header */}
      <div style={{ background: 'white', padding: '12px 16px', borderBottom: '1px solid #e2e8f0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <ArrowLeft size={20} style={{ cursor: 'pointer' }} onClick={onBack} />
          <div>
            <div style={{ fontSize: '0.85rem', fontWeight: 900, color: '#1e293b' }}>Home ▼</div>
            <div style={{ fontSize: '0.68rem', color: '#64748b' }}>Flat - 803, Ruby, Gulmohar Orch...</div>
          </div>
        </div>

        <div style={{ background: '#e6f4ea', color: '#0c831f', fontSize: '0.75rem', fontWeight: 800, padding: '6px 10px', borderRadius: '8px', textAlign: 'center', marginTop: '10px' }}>
          Yay! You saved ₹959 on this order 🎉
        </div>
      </div>

      {/* Cart Content */}
      <div style={{ padding: '14px', flex: 1 }}>
        {/* Coupons & Offers */}
        <div style={{ background: 'white', borderRadius: '16px', padding: '14px', marginBottom: '14px', boxShadow: '0 2px 8px rgba(0,0,0,0.03)' }}>
          <div style={{ fontSize: '0.8rem', fontWeight: 800, color: '#1e293b', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Ticket size={16} color="#ff3269" />
            Coupons & offers
          </div>

          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 0', borderBottom: '1px solid #f1f5f9' }}>
            <div>
              <div style={{ fontSize: '0.78rem', fontWeight: 800, color: '#1e293b' }}>Save ₹50 with Z-RAPIDOFF50</div>
              <div style={{ fontSize: '0.68rem', color: '#64748b' }}>View all coupons &gt;</div>
            </div>
            <button style={{ background: 'white', border: '1px solid #ff3269', color: '#ff3269', padding: '4px 12px', borderRadius: '8px', fontSize: '0.72rem', fontWeight: 800 }}>
              Apply
            </button>
          </div>

          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 0 0 0' }}>
            <div>
              <div style={{ fontSize: '0.78rem', fontWeight: 800, color: '#1e293b' }}>Save ₹15 with CREDZEP</div>
              <div style={{ fontSize: '0.68rem', color: '#64748b' }}>View all payment offers &gt;</div>
            </div>
            <button style={{ background: 'white', border: '1px solid #ff3269', color: '#ff3269', padding: '4px 12px', borderRadius: '8px', fontSize: '0.72rem', fontWeight: 800 }}>
              Apply
            </button>
          </div>
        </div>

        {/* ETA Card */}
        <div style={{ background: 'white', borderRadius: '16px', padding: '12px 14px', marginBottom: '14px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Clock size={18} color="#0c831f" />
            <div>
              <div style={{ fontSize: '0.8rem', fontWeight: 800, color: '#1e293b' }}>Delivering in 27 mins</div>
              <div style={{ fontSize: '0.68rem', color: '#64748b' }}>1 item</div>
            </div>
          </div>
          <button style={{ background: '#f1f5f9', border: 'none', padding: '4px 10px', borderRadius: '8px', fontSize: '0.72rem', fontWeight: 700, color: '#475569' }}>
            📅 Schedule
          </button>
        </div>

        {/* Cart Item Card */}
        <div style={{ background: 'white', borderRadius: '16px', padding: '14px', marginBottom: '14px', display: 'flex', gap: '12px', alignItems: 'center' }}>
          <div style={{ background: '#0f172a', borderRadius: '12px', padding: '8px', fontSize: '1.8rem', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            🎮
          </div>
          <div style={{ flex: 1 }}>
            <div style={{ fontSize: '0.78rem', fontWeight: 800, color: '#1e293b', lineHeight: 1.2 }}>
              Zebronics MAX FURY Transparent RGB LED Illumi...
            </div>
            <div style={{ fontSize: '0.68rem', color: '#64748b' }}>1 pc</div>
            <div style={{ fontSize: '0.85rem', fontWeight: 900, color: '#1e293b', marginTop: '4px' }}>
              ₹1080 <span style={{ textDecoration: 'line-through', fontSize: '0.7rem', color: '#94a3b8', fontWeight: 500 }}>₹1999</span>
            </div>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', border: '1px solid #ff3269', borderRadius: '8px', background: '#fff1f2' }}>
            <button style={{ border: 'none', background: 'none', color: '#ff3269', padding: '4px 8px', fontWeight: 800 }}>-</button>
            <span style={{ fontSize: '0.78rem', fontWeight: 800, color: '#ff3269' }}>1</span>
            <button style={{ border: 'none', background: 'none', color: '#ff3269', padding: '4px 8px', fontWeight: 800 }}>+</button>
          </div>
        </div>

        {/* PRODUCT HUNT PROGRESS & UNLOCKED COUPON CARD (Highlighted in mockup) */}
        <div className="cart-hunt-card" id="cart-hunt-card-target">
          <div style={{ display: 'flex', justifyContent: 'center', gap: '16px', marginBottom: '10px' }}>
            <div className="level-badge done"><Check size={14} /></div>
            <div className="level-badge done"><Check size={14} /></div>
            <div className="level-badge done" style={{ background: '#22c55e' }}><Check size={14} /></div>
          </div>

          <div className="coupon-code-badge">
            COUPON CODE: ACCZ50OFF
          </div>

          <div style={{ fontSize: '1.1rem', fontWeight: 900, color: '#15803d', marginTop: '2px' }}>
            Congratulations !!! 🎉
          </div>
          <div style={{ fontSize: '0.72rem', color: '#166534', marginTop: '2px' }}>
            Level 3 Complete! You unlocked ₹50 OFF + Free Delivery on this order.
          </div>
        </div>
      </div>

      {/* Bottom Sticky Payment Bar */}
      <div className="sticky-bottom-add" style={{ flexDirection: 'column', gap: '8px' }}>
        <div style={{ width: '100%', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div style={{ fontSize: '0.72rem', fontWeight: 700, color: '#64748b', display: 'flex', alignItems: 'center', gap: '4px' }}>
            <span>PAYING VIA</span>
            <span style={{ fontWeight: 800, color: '#5f259f' }}>PhonePe UPI</span>
          </div>
          <button
            style={{ background: '#f1f5f9', border: 'none', color: '#475569', fontSize: '0.7rem', fontWeight: 700, padding: '4px 8px', borderRadius: '6px' }}
            onClick={onResetDemo}
          >
            🔄 Reset Demo
          </button>
        </div>

        <button
          className="btn-add-cart-pink"
          onClick={() => {
            alert('🎉 Order Placed Successfully! Product Hunt Level 3 Milestone Completed!');
            onResetDemo();
          }}
        >
          Pay ₹1080
        </button>
      </div>
    </div>
  );
}
