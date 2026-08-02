import React from 'react';

export function GuidedTutorialOverlay({ currentStep, totalSteps, stepData, onNext, onPrev, onSkip }) {
  if (!stepData || currentStep <= 0) return null;

  return (
    <>
      {/* Background Mask */}
      <div className="tutorial-overlay-mask" onClick={onNext} />

      {/* Target Cutout Highlight Box */}
      {stepData.targetRect && (
        <div
          className="highlight-cutout"
          style={{
            top: `${stepData.targetRect.top}px`,
            left: `${stepData.targetRect.left}px`,
            width: `${stepData.targetRect.width}px`,
            height: `${stepData.targetRect.height}px`,
          }}
        />
      )}

      {/* Tutorial Tooltip Card */}
      <div
        className="tutorial-tooltip-card"
        style={{
          top: stepData.tooltipTop ? `${stepData.tooltipTop}px` : 'auto',
          bottom: stepData.tooltipBottom ? `${stepData.tooltipBottom}px` : 'auto',
        }}
      >
        <div className="tutorial-step-badge">
          STEP {currentStep} OF {totalSteps} • GUIDED MVP TOUR
        </div>
        <h3 className="tutorial-title">{stepData.title}</h3>
        <p className="tutorial-desc">{stepData.description}</p>

        <div className="tutorial-btn-row">
          <button className="btn-tut-skip" onClick={onSkip}>
            Skip Guided Tour
          </button>
          <div style={{ display: 'flex', gap: '8px' }}>
            {currentStep > 1 && (
              <button
                className="btn-tut-skip"
                style={{ color: '#475569', fontWeight: 600 }}
                onClick={onPrev}
              >
                Back
              </button>
            )}
            <button className="btn-tut-next" onClick={onNext}>
              {currentStep === totalSteps ? 'Got it! 🎉' : stepData.buttonText || 'Next Step →'}
            </button>
          </div>
        </div>
      </div>
    </>
  );
}
