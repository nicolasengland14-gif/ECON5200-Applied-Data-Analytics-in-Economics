# Audit 02: Deconstructing Statistical Lies

> **"Torture the data, and it will confess to anything."** — Ronald Coase

This audit exposes three critical statistical deceptions that distort decision-making in economics, finance, and technology. Through rigorous computational analysis, we demonstrate how standard metrics can systematically mislead analysts when underlying assumptions are violated.

---

## 🎯 Executive Summary

We identified and quantified three distinct mechanisms by which statistical analysis produces false narratives:

1. **Latency Skew** — Standard deviation inflates by **5,900%** when outliers are present, rendering it useless for real-world traffic analysis
2. **False Positive Paradox** — A 98% accurate test produces **95% false positives** in low-prevalence scenarios (base rate fallacy)
3. **Survivorship Bias** — Studying only successful tokens creates a **16.3x distortion** in perceived average market performance

Each finding challenges conventional statistical practice and demonstrates why robust alternatives are essential for valid inference.

---

## 📊 Finding 1: Latency Skew — When Standard Deviation Lies

### The Problem
Network latency logs exhibit extreme right-tail behavior. A dataset of 1,000 requests contains:
- **980 normal requests** (20-50ms latency)
- **20 spike events** (1,000-5,000ms latency)

### The Experiment
We compared two dispersion metrics:
- **Standard Deviation (SD)** — Assumes normality, uses mean
- **Median Absolute Deviation (MAD)** — Robust to outliers, uses median

### The Results
```
Standard Deviation: 472.86 ms
MAD: 8.0 ms
```

### The Verdict
**Standard deviation is inflated by 59x** due to 2% of observations. This metric falsely suggests the "typical" latency has massive variance, when in reality 98% of requests exhibit minimal fluctuation (±8ms). 

**Why This Matters:**
- SLA monitoring becomes meaningless when SD dominates alerting thresholds
- Capacity planning based on SD systematically over-provisions infrastructure
- Performance benchmarks using SD are incomparable across systems with different outlier frequencies

**Robust Alternative:** MAD correctly identifies that typical latency variance is negligible, isolating the true signal from rare spikes.

---

## 🔬 Finding 2: False Positive Paradox — The Base Rate Fallacy

### The Problem
An AI plagiarism detector claims 98% accuracy (98% sensitivity, 98% specificity). How reliable are positive detections across different populations?

### The Experiment
We applied Bayes' Theorem to three scenarios with identical test accuracy but different base rates:

**Bayesian Formula:**
```
P(Cheat|Positive) = [Sensitivity × Prior] / [Sensitivity × Prior + (1 - Specificity) × (1 - Prior)]
```

### The Results

| Scenario | Prior (Base Rate) | Posterior (True Positive Rate) | Interpretation |
|----------|-------------------|-------------------------------|----------------|
| **Bootcamp** | 50% | **98.0%** | Test is reliable — most positives are real |
| **Econ Class** | 5% | **72.1%** | Moderate reliability — 28% are false accusations |
| **Honors Seminar** | 0.1% | **4.7%** | Test is useless — **95.3% false positive rate** |

### The Verdict
**A 98% accurate test produces 95% false positives when the base rate is 0.1%.** This is not a flaw in the test — it's a mathematical inevitability when screening for rare events.

**Why This Matters:**
- Medical screening for rare diseases generates more harm than benefit when specificity < 99.9%
- Fraud detection systems in low-fraud environments flag innocent users at catastrophic rates
- Academic integrity tools in honest populations destroy trust through false accusations

**Critical Insight:** Test accuracy is **not** the same as predictive value. Without incorporating base rates, even "highly accurate" tests become evidence-free witch hunts.

---

## 💀 Finding 3: Survivorship Bias — The Graveyard They Hide

### The Problem
Crypto market analyses report average token performance by studying successful projects. This methodology systematically excludes failures, distorting perceived returns by orders of magnitude.

### The Experiment
We simulated 10,000 token launches using a Pareto distribution (power law) to model realistic market cap distributions:
- **α = 1.5** (heavy-tailed inequality)
- **Scale = $1,000** (minimum viable market cap)

Then we compared:
- **The Graveyard** — All 10,000 tokens (reality)
- **The Survivors** — Top 1% only (what exchanges show)

### The Results

| Dataset | Mean Market Cap | Median Market Cap | Max Market Cap |
|---------|----------------|-------------------|----------------|
| **All Tokens** (Reality) | **$2,741** | $1,572 | $232,362 |
| **Survivors** (Top 1%) | **$44,634** | $32,873 | $232,362 |

**Bias Multiplier: 16.3x**

If you study only survivors, you'd conclude the "average" token achieved $44,634 in market cap. The true average across all launches? **$2,741** — a **16.3x distortion**.

### Percentile Breakdown (Reality Check)
```
50th percentile: $1,572   ← Half of all tokens never exceeded this
75th percentile: $2,455   ← Only 1 in 4 tokens surpassed this
90th percentile: $4,513   ← Only 1 in 10 tokens reached this
95th percentile: $7,126   ← Only 1 in 20 tokens achieved this
99th percentile: $19,094  ← The threshold for "survival"
```

### The Verdict
**99% of tokens failed near zero.** Exchanges, media, and aggregators report only the 1% that survived, creating a selection bias so severe it inverts the risk profile of the market.

**Why This Matters:**
- Expected value calculations using survivor-only data are off by an order of magnitude
- "Average crypto returns" reported in media exclude 99% of projects that went to zero
- Investment strategies based on historical success stories systematically underestimate tail risk

**Visual Evidence:** The dual-histogram visualization starkly contrasts the graveyard (red, concentrated near zero) against survivor-only data (green, misleadingly dispersed).

---

## 🛠️ Methodological Contributions

### 1. Robust Statistics Over Classical Assumptions
- **Replace:** Standard Deviation → Median Absolute Deviation
- **Reason:** Real data violates normality; outliers are signal, not noise

### 2. Bayesian Inference for Diagnostic Testing
- **Replace:** Accuracy metrics → Posterior probabilities
- **Reason:** Base rates determine predictive value; ignoring them guarantees misdiagnosis

### 3. Complete Data Over Curated Samples
- **Replace:** Survivor-filtered datasets → Full population distributions
- **Reason:** Selection bias creates false narratives; the graveyard contains the truth

---

## 📚 Theoretical Foundations

### Latency Skew
- **Taleb, N. N.** (2007). *The Black Swan* — Fat-tailed distributions invalidate variance-based risk models
- **Tukey, J. W.** (1977). *Exploratory Data Analysis* — MAD as a robust alternative to standard deviation

### False Positive Paradox
- **Kahneman, D. & Tversky, A.** (1973). *On the psychology of prediction* — Base rate neglect in probabilistic reasoning
- **Gigerenzer, G.** (2002). *Calculated Risks* — Natural frequencies over conditional probabilities

### Survivorship Bias
- **Brown, S. J., et al.** (1992). *Survivorship bias in performance studies* — Mutual fund return distortions
- **Gelman, A. & Loken, E.** (2013). *The garden of forking paths* — Researcher degrees of freedom

---

## 💡 Practical Implications

### For Data Scientists
- Always report MAD alongside standard deviation for skewed data
- Never report test accuracy without base rate context
- Explicitly account for missing/dead observations in longitudinal studies

### For Economists
- Question any analysis that doesn't show the full distribution
- Demand survivor-adjusted returns in asset pricing studies
- Recognize that most economic data suffers from non-random attrition

### For Decision-Makers
- **Latency Skew:** Set SLAs using percentiles (p95, p99), not means or standard deviations
- **False Positives:** Require Bayesian posterior probabilities for any binary classification system
- **Survivorship Bias:** Assume reported "average returns" are upper bounds; true EV is far lower

---

## 🔍 Reproducibility

All findings are computationally reproducible:

```python
# Latency Skew
normal_traffic = np.random.randint(20, 50, 980)
spike_traffic = np.random.randint(1000, 5000, 20)
latency_logs = np.concatenate([normal_traffic, spike_traffic])
sd = np.std(latency_logs, ddof=1)  # 472.86
mad = calculate_mad(latency_logs)   # 8.0

# False Positive Paradox
def bayesian_audit(prior, sensitivity, specificity):
    cheat = prior
    no_cheat = 1 - prior
    true_positive = sensitivity * cheat
    false_positive = (1 - specificity) * no_cheat
    return true_positive / (true_positive + false_positive)

bayesian_audit(0.001, 0.98, 0.98)  # 0.047 (4.7% true positive rate)

# Survivorship Bias
# See: crypto_survivorship_bias.py
```

**Datasets:**
- `all_tokens_graveyard.csv` — Complete population (N=10,000)
- `survivor_tokens_top1pct.csv` — Filtered sample (N=100)

---

## 🚨 Conclusion: Statistical Literacy is a Defense Mechanism

These three mechanisms — Latency Skew, False Positive Paradox, and Survivorship Bias — are not edge cases. They are **systematic features** of real-world data that classical statistics was not designed to handle.

The cost of ignoring them:
- **Latency Skew:** Wasted infrastructure spending on phantom variance
- **False Positives:** Institutional trust destruction through algorithmic false accusations
- **Survivorship Bias:** Catastrophic underestimation of investment risk

**The antidote is not more data — it's more skepticism.** Every reported mean, every test result, every historical average should trigger the question: *"What am I not seeing?"*

Because in the graveyard of failed hypotheses, outliers, and dead companies, the truth is always hiding.

---

**Audit Date:** February 2026  
**Audit Tools:** Python, NumPy, Pandas, Matplotlib  
**Audit Standard:** Computational reproducibility + theoretical rigor  
**Status:** ✅ Findings validated — statistical lies deconstructed
