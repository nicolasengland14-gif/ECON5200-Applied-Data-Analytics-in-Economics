Script Architecture
The script exposes three clean, composable functions:
FunctionRolestandardised_mean_diff(df)Core SMD estimator using pooled variance denominatorbuild_balance_table(...)Constructs a tidy balance DataFrame, sorted by worst pre-match imbalanceplot_love(...)Renders the dual-panel Love Plot with band annotationsprint_balance_summary(...)Prints a full diagnostic table to stdout
The SMD formula used is the Rosenbaum-Rubin (1985) formulation:

SMD = (μ_T − μ_C) / √[(σ²_T + σ²_C) / 2]

This is preferred over a pooled t-statistic because it is sample-size invariant — critical when matched samples are much smaller than the original.

Visual Evidence Required to Prove Bias Mitigation
For a Love Plot to conclusively demonstrate selection bias elimination, five conditions must hold simultaneously:
1. All post-match points must cross into the green zone (|SMD| ≤ 0.10). The 0.10 threshold, codified by Stuart (2010) and the What Works Clearinghouse, is the field-standard for "acceptable" balance. The 0.20 amber band indicates marginal cases that require theoretical justification. Any covariate remaining in the red zone is a fatal threat to causal identification.
2. The connecting lines must point uniformly leftward. This directional consistency proves that matching systematically reduced — never worsened — imbalance across all covariates. A rightward-moving line signals that your matching algorithm degraded balance on that variable, often due to poor caliper choice or insufficient common support.
3. Mean |SMD| reduction should exceed ~80%. The secondary bar panel quantifies this. An 87.5% overall reduction (as in the demo) constitutes strong evidence. Values below 50% suggest the propensity model is misspecified or common support is thin.
4. No "reversal of sign." The absolute SMD hides sign changes. If a covariate flips from over-represented to under-represented post-match, the net |SMD| may look fine but introduce a new bias. A robustness check is to plot raw (signed) SMDs in addition.
5. The plot must be accompanied by balance on higher-order moments. SMD only tests mean differences. For non-linear treatment effect heterogeneity, you should additionally verify variance ratios (target: 0.5 – 2.0) and empirical CDF overlap (Kolmogorov-Smirnov test). The Love Plot is necessary but not alone sufficient.
The demo output shows 7/9 covariates fully balanced, with health_score and income sitting in the amber zone — real-world PSM nearly always produces this pattern, which is why doubly-robust estimators (IPW + regression adjustment) are recommended as a follow-up when any covariate remains marginal.
