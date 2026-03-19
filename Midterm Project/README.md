For my midterm project, I have chosen to study, Card, D., & Krueger, A. B. (1994). Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania.
Linked here: https://davidcard.berkeley.edu/papers/njmin-aer.pdf
This paper aims to answer questions surrounding the effect of raising the minimum wage, specifically, how this impacts the rate of employment at fast-food restaraunts in New Jersey and Pennsylvania. The authors, David Card and Alan B Krueger, monitored 410 fast-food locations before and after the increawse of the minimum wage in New Jersey from $4.25 to $5.05, to figure out if low-wage labor markets are effected like those before them had hypothesized. 

# Card & Krueger (1994) Replication and Extension  
### Difference-in-Differences Analysis of Minimum Wage Effects

## 📌 Project Overview

This project replicates the seminal paper:

**Card, D., & Krueger, A. B. (1994)**  
*"Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania."*

The original study examines whether an increase in the minimum wage in New Jersey (from $4.25 to $5.05 in April 1992) led to changes in employment relative to Pennsylvania, where the minimum wage remained unchanged.

Using a Difference-in-Differences (DID) framework, this project reconstructs the analysis and evaluates the causal impact of the policy change.

---

## 🎯 Research Question

Did the 1992 minimum wage increase in New Jersey reduce employment in fast-food restaurants compared to Pennsylvania?

---

## ⚙️ Methodology

### Core Approach: Difference-in-Differences (DID)

- **Treatment Group:** New Jersey restaurants  
- **Control Group:** Pennsylvania restaurants  
- **Pre/Post Period:** Before and after April 1992  

The DID estimator compares changes in employment across these groups to isolate the causal effect of the policy.

---

## 🧹 Data & Cleaning

The original dataset (`public.dat`) is a fixed-width file requiring custom ingestion.

Key steps:
- Imported raw data using `pandas`
- Handled missing values (e.g., `"."`)
- Converted variables to numeric types
- Constructed **Full-Time Equivalent (FTE)** employment:

---

## 📊 Replication Results

The replication follows three key steps:

### 1. Descriptive Statistics
- Calculated means and standard deviations by state and time period

### 2. Manual DID Calculation
- Computed the difference in employment changes between NJ and PA

### 3. Regression Analysis

Model:

- Estimated using `statsmodels`
- Clustered standard errors at the store level

### ✅ Key Finding:
The estimated treatment effect is **positive**, consistent with Card & Krueger (1994), suggesting no evidence of employment decline following the minimum wage increase.

---

## 🔍 Extension: Testing the Parallel Trends Assumption

### Approach: Data Enrichment

To strengthen the validity of the DID design, this project incorporates external macroeconomic data from **FRED**.

- Data used: State-level unemployment rates (NJ vs PA)
- Time period: 1990–1992 (pre-treatment)

### Purpose:
To evaluate whether both states followed similar labor market trends prior to the policy change.

### 📈 Result:
Pre-treatment unemployment trends in New Jersey and Pennsylvania move similarly, supporting the **parallel trends assumption**.

---

## 🧠 Conclusion

The replication confirms the original finding that the minimum wage increase did not reduce employment in fast-food restaurants.

The extension further strengthens the credibility of this result by providing external evidence that the treatment and control groups were on similar trajectories prior to the policy change.

---

## 📁 Repository Structure

---

## 🛠️ Tools & Technologies

- Python (pandas, numpy)
- statsmodels
- matplotlib
- fredapi (FRED data)

---

## 📌 How to Run

1. Clone the repository  
2. Open notebooks in Jupyter or Google Colab  
3. Add your FRED API key in the extension notebook  
4. Run all cells sequentially  

---

## 👤 Author

Nicolas  
Northeastern University — Economics
