# The Cost of Living Crisis: A Data-Driven Analysis

## Executive Summary

This project investigates whether traditional Consumer Price Index (CPI) metrics accurately represent the lived economic reality of university students in the Boston metropolitan area. Through custom index construction and regional comparative analysis, I reveal a counterintuitive finding: while national inflation surged 37.19% between 2016-2025, student-specific costs increased only 32.41%—a 4.77 percentage point divergence that challenges conventional narratives about the student debt crisis.

---

## The Problem: Why the "Average" CPI Fails Students

The Bureau of Labor Statistics' CPI tracks a basket of goods representative of urban households, but this "average" consumer doesn't exist. Students face a fundamentally different economic reality:

- **Tuition inflation** operates independently of general price dynamics
- **Geographic concentration** in high-cost metros like Boston amplifies regional disparities  
- **Consumption patterns** skew heavily toward education, housing, and digital services—not the BLS's representative basket

Traditional CPI metrics risk obscuring demographic-specific price pressures, potentially leading to misallocated policy interventions. This analysis constructs a Student-Specific Price Index (SPI) to quantify these gaps empirically.

---

## Methodology: Python, APIs, and Index Theory

### Data Infrastructure

**Data Sources:**
- **FRED API** (`pandas_datareader`): National CPI-U (CPIAUCSL) and Boston-Cambridge-Newton CPI (CUURA103SA0)
- **Custom tracking data**: Northeastern University costs, Chick-fil-A pricing, Honda Civic MSRP, Netflix subscription rates (2016-2025)

**Technology Stack:**
```
Python 3.12 | pandas 2.x | matplotlib | pandas_datareader
```

### Index Construction Methodology

I employed a **modified Laspeyres Index** approach to construct the Student-Specific Price Index:

**Laspeyres Formula:**
```
SPI_t = Σ(P_i,t / P_i,0) × w_i × 100
```

Where:
- `P_i,t` = Price of item i at time t
- `P_i,0` = Base period price (Jan 1, 2016)
- `w_i` = Weight of item i in student budget

**Weight Allocation (Based on Student Expenditure Patterns):**
- Northeastern Total Costs: **60%** (tuition, fees, room & board)
- Transportation (Honda Civic): **15%** (commuting, ownership costs)
- Food (Chick-fil-A Spicy Deluxe): **15%** (dining out, quick service)
- Entertainment (Netflix): **10%** (streaming, digital subscriptions)

**Normalization:**  
All indices rebased to Jan 1, 2016 = 100 for direct comparability across National CPI, Boston Regional CPI, and Student SPI.

### Regional Comparison Framework

To isolate geographic vs. demographic effects, I decomposed total student price pressure into:
1. **Boston Regional Premium**: Local CPI deviation from national average
2. **Student Demographic Premium**: SPI deviation from local CPI

This two-stage analysis distinguishes whether students face elevated costs due to geography (Boston is expensive) or consumption patterns (student budgets are unique).

---

## Key Findings

### 1. The Student Deflation Paradox

**My analysis reveals a 4.77 percentage point divergence between Student SPI and National CPI over the 2016-2025 period.**

- **National CPI (Dec 2025):** 137.19 (+37.19% vs. 2016 baseline)
- **Student SPI (Dec 2025):** 132.41 (+32.41% vs. 2016 baseline)
- **Divergence:** -4.77 points

**Interpretation:**  
Contrary to media narratives about runaway student costs, students in this cohort experienced *lower* inflation than the general population. This likely reflects:
- Moderated tuition growth at Northeastern (possibly due to frozen rates during COVID-19)
- Deflationary pressures in durable goods (vehicles) and technology services (streaming)
- Exclusion of volatile categories like energy/food commodities that drove headline CPI

### 2. The Boston Regional Discount

**Boston CPI tracked 1.93 points BELOW National CPI by December 2025:**

- **Boston CPI:** 135.25 (+35.25%)
- **National CPI:** 137.19 (+37.19%)
- **Regional Premium:** -1.93 points

This counterintuitive finding suggests that during this inflationary period, Boston's economy—anchored by education, healthcare, and technology sectors—experienced relatively contained price growth compared to national trends driven by supply chain disruptions and energy volatility.

### 3. Decomposition of Student Economic Reality

```
Total Student vs. National Gap: -4.77 points
├─ Boston Regional Effect:     -1.93 points (40.5%)
└─ Student Demographic Effect:  -2.84 points (59.5%)
```

The majority of the student advantage stems from consumption basket differences (demographic effect), not location (regional effect). This has critical implications for policy: targeted interventions must address *what* students buy, not just *where* they live.

---

## Technical Implementation Highlights

### Challenge 1: Handling Missing Data
Boston CPI is published monthly/bimonthly with irregular gaps. I implemented forward-fill imputation:
```python
df['Boston_CPI'] = df['Boston_CPI'].ffill()
```

### Challenge 2: Index Rebasing
Ensured temporal alignment by normalizing all series to a common baseline:
```python
baseline_value = boston_cpi_raw.loc['2016-01-01', 'Boston_CPI_Raw']
boston_cpi_raw['Boston_CPI'] = (boston_cpi_raw['Boston_CPI_Raw'] / baseline_value) * 100
```

### Challenge 3: Weighted Index Construction
Custom SPI calculation from heterogeneous price series:
```python
df['Student_SPI'] = (
    normalized_components['Northeastern Total Costs'] * 0.60 +
    normalized_components['Honda Civic'] * 0.15 +
    normalized_components['Chick-Fil-A Spicy Deluxe'] * 0.15 +
    normalized_components['Basic Netflix Subscription'] * 0.10
)
```

---

## Visualization & Communication

The three-line comparative chart provides immediate visual evidence of the divergence:

- **Grey (National CPI):** Steepest trajectory, reflecting broad inflationary pressures
- **Blue (Boston CPI):** Moderate path, regional economic composition shields from national volatility
- **Red (Student SPI):** Flattest trajectory, demonstrating demographic-specific price dynamics

Clear labeling and a normalized baseline (Jan 2016 = 100) allow stakeholders to instantly grasp relative performance without statistical expertise.

---

## Business & Policy Implications

1. **Student Loan Policy:** If student costs are rising *slower* than general inflation, blanket debt forgiveness may be poorly targeted. Income-driven repayment adjustments should reflect actual SPI growth, not CPI.

2. **University Financial Planning:** Northeastern's cost trajectory suggests effective cost containment during 2016-2025. This should inform future tuition-setting strategies.

3. **Regional Economic Analysis:** Boston's below-national inflation challenges assumptions about "expensive coastal cities." Sector composition matters more than geography alone.

4. **Inflation Metrics Reform:** BLS should publish demographic-specific indices (Student CPI, Senior CPI, etc.) to inform targeted policy interventions.

---

## Limitations & Future Work

**Limitations:**
- Small sample size (n=4 goods) limits generalizability
- Weights are illustrative, not empirically derived from expenditure surveys
- Excludes healthcare, textbooks, technology hardware (data availability constraints)
- Single institution (Northeastern) may not represent national trends

**Future Enhancements:**
- Expand basket to 20+ items using IPEDS data for tuition, BLS CES for wages
- Conduct sensitivity analysis on weight allocations
- Extend geographic comparison to 10+ metro areas
- Build interactive dashboard for real-time SPI tracking

---

## Reproducibility

**Code Repository:** [GitHub - Student CPI Analysis]  
**Data Sources:** FRED API (publicly accessible), custom tracking spreadsheet  
**Dependencies:** `requirements.txt` included  

All analysis is fully reproducible with documented Python scripts and archived data snapshots.

---

## Conclusion

This project demonstrates that **data science can challenge dominant narratives** when applied rigorously. By constructing a Student-Specific Price Index and comparing it to regional and national benchmarks, I revealed a 4.77 percentage point gap that contradicts conventional wisdom about student cost burdens.

The methodological contributions—custom index construction, regional decomposition, and API-driven data pipelines—are transferable to other demographic or sector-specific inflation analyses. In an era of heated debate about inflation and inequality, this work shows that careful measurement matters: sometimes the crisis isn't where the headlines say it is.

---

**Skills Demonstrated:** Python (pandas, matplotlib), API Integration, Economic Index Theory, Statistical Analysis, Data Visualization, Technical Communication

**Impact:** Provides empirical foundation for evidence-based student financial policy reform
