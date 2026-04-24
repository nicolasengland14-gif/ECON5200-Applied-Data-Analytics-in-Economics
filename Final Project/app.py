import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Police and Crime Dashboard", layout="wide")
st.title("Consulting Report: Police Presence and Crime")


st.sidebar.header("What-If Scenario")

treatment_multiplier = st.sidebar.slider(
    "Change in Police per Capita",
    min_value=0.5, max_value=3.0, value=1.0, step=0.1
)

baseline_ate = 1.2246
baseline_se = 0.791

adjusted_ate = baseline_ate * treatment_multiplier
adjusted_se = baseline_se * treatment_multiplier

ci_lower = adjusted_ate - 1.96 * adjusted_se
ci_upper = adjusted_ate + 1.96 * adjusted_se

col1, col2, col3 = st.columns(3)

col1.metric("Estimated Effect", f"{adjusted_ate:.3f}")
col2.metric("95% CI Lower", f"{ci_lower:.3f}")
col3.metric("95% CI Upper", f"{ci_upper:.3f}")

st.markdown(f"""
### Interpretation

If police presence changes by **{treatment_multiplier:.1f}x**,  
the estimated effect on crime is **{adjusted_ate:.3f}**  
(95% CI: [{ci_lower:.3f}, {ci_upper:.3f}]).
""")


multipliers = np.arange(0.5, 3.1, 0.1)
ates = baseline_ate * multipliers
ses = baseline_se * multipliers

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=multipliers,
    y=ates + 1.96 * ses,
    mode="lines",
    line=dict(width=0),
    showlegend=False
))

fig.add_trace(go.Scatter(
    x=multipliers,
    y=ates - 1.96 * ses,
    mode="lines",
    fill="tonexty",
    fillcolor="rgba(0,100,200,0.2)",
    line=dict(width=0),
    name="95% CI"
))

fig.add_trace(go.Scatter(
    x=multipliers,
    y=ates,
    mode="lines",
    line=dict(width=3),
    name="Estimated Effect"
))

fig.update_layout(
    title="Effect vs. Change in Police Presence",
    xaxis_title="Multiplier",
    yaxis_title="Estimated Effect",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Counterfactual Scenario")

cf_ate = baseline_ate * 2
cf_low = cf_ate - 1.96 * baseline_se * 2
cf_high = cf_ate + 1.96 * baseline_se * 2

st.write(
    f"If police presence doubled, the estimated effect would be "
    f"**{cf_ate:.3f}** (95% CI: [{cf_low:.3f}, {cf_high:.3f}])."
)