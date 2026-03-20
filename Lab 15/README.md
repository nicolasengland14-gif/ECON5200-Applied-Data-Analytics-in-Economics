## Forecasting Architecture and the Bias-Variance Tradeoff

**Objective:** To empirically diagnose the bias-variance tradeoff by engineering a deliberately overfit polynomial regression model on real corporate financial data, then quantifying its true generalization failure through rigorous cross-validation.

---

### Methodology

- **Data Sourcing:** Collected NVIDIA's quarterly total corporate revenue across 2024–2026, establishing a small, high-signal time-series dataset representative of real-world constraints in financial forecasting contexts.

- **Polynomial Feature Expansion:** Applied a 7th-degree polynomial transformation via `scikit-learn`'s `PolynomialFeatures`, dramatically increasing model complexity and degrees of freedom relative to the available observations — a deliberate architectural decision to induce high variance.

- **In-Sample vs. Out-of-Sample Evaluation:** Measured training MSE to confirm near-zero in-sample error, then generated an extrapolated out-of-sample forecast to expose catastrophic predictive breakdown — a canonical symptom of overfitting.

- **K-Fold Cross-Validation:** Applied K-Fold CV via `cross_val_score` to compute a statistically robust estimate of true operational error, bypassing the optimistic bias of training error and surfacing the model's real generalization capacity.

---

### Key Findings

A 7th-degree polynomial expansion achieved near-zero training MSE — a superficially strong result that masked severe structural instability. When the model was tasked with extrapolating to an out-of-sample quarter, it produced hallucinated predictions orders of magnitude removed from plausible values, confirming the hallmark failure mode of high-variance estimators.

K-Fold Cross-Validation subsequently revealed a true operational error vastly exceeding the training error, quantifying the generalization gap with statistical rigor. These results constitute a controlled proof-of-concept: unconstrained model complexity, in the absence of regularization, produces forecasting architectures that are not merely imprecise — they are operationally unreliable. The findings underscore regularization (L1/L2 penalty terms, polynomial degree constraints) as a non-negotiable design requirement in any production forecasting pipeline operating under data scarcity.

---

**Stack:** Python · pandas · NumPy · scikit-learn (`PolynomialFeatures`, `LinearRegression`, `cross_val_score`) · Matplotlib
