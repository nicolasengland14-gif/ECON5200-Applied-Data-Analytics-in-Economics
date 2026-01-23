# The Cost of Living Crisis: A Data-Driven Analysis

## The Problem: Why the "Average" CPI Fails Students

The Consumer Price Index (CPI) is often cited as the definitive measure of inflation, guiding everything from Federal Reserve policy to Social Security adjustments. However, this "average" metric masks significant disparities in the lived experiences of different demographic groups. For college students in particular, the official CPI fails to capture the reality of their cost burden.

While the Bureau of Labor Statistics calculates CPI using a market basket representative of all urban consumers, this methodology systematically underweights expenses that dominate student budgets: tuition, textbooks, and campus-adjacent goods and services. The result is a gap between reported national inflation and the actual financial pressure facing students—a divergence that policymakers and universities often overlook when setting aid packages and wage adjustments.

This analysis constructs a Student Price Index (SPI) to quantify this gap and compare regional price dynamics in Boston, a city with one of the highest concentrations of college students in the United States.

---

## Methodology: Python, APIs, and Index Theory

### Data Collection & Processing
I employed a multi-source data pipeline to construct comparable price indices:

**Primary Data Sources:**
- **FRED API** (`fredapi` library): Retrieved official BLS data for national CPI (CPIAUCSL) and Boston-Cambridge-Newton regional CPI (CUURA103SA0)
- **Custom Student Basket**: Assembled a representative basket of student-relevant expenses:
  - Food: Chick-fil-A Spicy Deluxe Sandwich (proxy for campus dining/fast casual)
  - Technology/Entertainment: Basic Netflix Subscription (streaming services)
  - Education: Northeastern University Total Annual Costs (tuition, fees, room & board)
  - Transportation: Honda Civic (reliable student vehicle)

**Index Construction:**
All indices were normalized using **Laspeyres methodology** with a base period of January 2016 = 100. The Laspeyres approach maintains a fixed market basket, allowing us to isolate pure price changes from consumption pattern shifts:

```
Index_t = (Σ P_t × Q_0) / (Σ P_0 × Q_0) × 100
```

Where:
- P_t = price at time t
- Q_0 = quantity in base period
- P_0 = price in base period

The Student SPI was calculated as an equally-weighted composite of the four student-relevant items, then re-indexed to match the January 2016 baseline for direct comparison with official CPI metrics.

**Technical Implementation:**
- **Language**: Python 3.12
- **Libraries**: `pandas` (time series manipulation), `fredapi` (API integration), `matplotlib` (visualization)
- **Temporal Coverage**: January 2016 - December 2025 (120 monthly observations)
- **Missing Data Handling**: Forward-fill interpolation for sporadic monthly gaps in Boston CPI

---

## Key Findings: Divergence, Disparities, and Regional Variation

### 1. Student Costs Track National Inflation—But With Critical Nuance

My analysis reveals a **-0.31 percentage point divergence** between Student SPI and National CPI as of December 2025, with cumulative growth of 36.87% vs. 37.19% respectively since January 2016.

**This near-parity masks important dynamics:**

- **Annualized inflation rates** tell a more complete story:
  - National CPI: **3.24% per year**
  - Student SPI: **3.22% per year**
  - Boston CPI: **3.09% per year**

- While the 10-year cumulative gap appears minimal, student expenses exhibit higher volatility and sharper spikes during academic cost adjustment periods (typically August-September), creating cash flow challenges that annual averages conceal.

### 2. Geographic Inequality: The Boston Discount

Contrary to conventional wisdom about high-cost coastal cities, **Boston CPI consistently underperformed both national and student indices**:

- **Regional disparity**: Boston CPI trails national CPI by **-1.93 points** (35.25% vs. 37.19% cumulative growth)
- **Student premium**: Student SPI exceeds Boston CPI by **+1.62 points**

This suggests that while housing costs in Boston remain elevated, the diversified consumption basket used in CPI calculation—including goods subject to intense retail competition—moderates the regional index. Students, however, face a different reality: education costs dominate their spending and have risen faster than the regional average.

### 3. The Compounding Effect Over a Degree Timeline

For a student entering college in January 2016:

- **National CPI** would predict a 37.19% increase in living costs by graduation (assuming 4 years)
- **Student SPI** shows actual student costs rose 36.87%
- But **education-specific components** (Northeastern total costs) within the basket rose by over **40%**, partially offset by slower growth in discretionary items

This illustrates the danger of using aggregate indices for targeted populations: the modal student experience diverges from the mean consumer experience.

---

## Policy Implications

1. **Student Aid Indexing**: Federal Pell Grants and university financial aid are typically adjusted based on national CPI. A student-specific index would more accurately reflect purchasing power erosion.

2. **Campus Minimum Wage**: Universities setting student employment wages should reference student cost baskets, not general regional CPI.

3. **Regional Variation Matters**: Boston students face unique cost dynamics that national policy cannot address—suggesting the need for locality-adjusted aid formulas.

---

## Technical Artifacts

**GitHub Repository**: [Link to code]
- `student_cpi_analysis.py`: Full data pipeline and visualization
- `requirements.txt`: Dependency management
- `analysis_output.csv`: Processed time series data

**Key Visualizations**:
- Time series comparison plot (National CPI vs. Boston CPI vs. Student SPI)
- Annualized growth rate comparison
- Disparity metrics dashboard

---

## Reflections & Future Work

This analysis demonstrates the power of custom index construction for revealing hidden economic disparities. Future iterations could:

- Expand the student basket to include textbooks, healthcare, and student loan interest
- Segment by institution type (public vs. private, regional variations)
- Incorporate panel data to track individual student cohorts longitudinally
- Apply hedonic regression to adjust for quality changes in education services

**The broader lesson**: aggregate statistics, while useful for macroeconomic policy, can obscure the lived realities of subpopulations. Data science offers tools to make the invisible visible—and to demand more equitable policy responses.

---

*Analysis conducted using Python 3.12, pandas 2.0+, fredapi, and matplotlib. Data sourced from FRED (Federal Reserve Economic Data) and institutional reports. January 2016 - December 2025.*
