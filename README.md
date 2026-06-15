# Mutual Fund Analytics Capstone

## Overview

The Mutual Fund Analytics Capstone is an end-to-end data analytics project developed as part of the Bluestock Fintech Internship Program. The project focuses on collecting, cleaning, storing, analyzing, and visualizing mutual fund industry data using Python, SQLite, and Power BI.

The solution combines ETL pipelines, exploratory data analysis (EDA), performance analytics, risk metrics, and interactive dashboard development to generate actionable insights into mutual fund performance, investor behavior, industry growth trends, and SIP market dynamics.

---

## Project Objectives

* Build a complete ETL pipeline for mutual fund datasets.
* Validate and clean raw financial data.
* Store processed data in a SQLite database.
* Perform exploratory data analysis and statistical profiling.
* Calculate advanced performance and risk metrics.
* Develop an interactive Power BI dashboard.
* Generate business insights and recommendations.
* Deliver professional documentation and presentation materials.

---

## Technology Stack

### Programming & Analysis

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

### Database

* SQLite

### Visualization

* Power BI Desktop

### Version Control

* Git
* GitHub

---

## Dataset Description

The project uses ten core mutual fund datasets:

| Dataset                  | Description                          |
| ------------------------ | ------------------------------------ |
| 01_fund_master           | Fund metadata and scheme information |
| 02_nav_history           | Historical NAV values                |
| 03_aum_by_fund_house     | Assets Under Management by AMC       |
| 04_monthly_sip_inflows   | Monthly SIP statistics               |
| 05_category_inflows      | Category-wise fund inflows           |
| 06_industry_folio_count  | Industry folio statistics            |
| 07_scheme_performance    | Fund return and performance metrics  |
| 08_investor_transactions | Investor transaction records         |
| 09_portfolio_holdings    | Fund portfolio holdings              |
| 10_benchmark_indices     | Benchmark index performance          |

Additional analytical datasets include:

* alpha_beta.csv
* fund_scorecard.csv
* sharpe_values.csv
* sortino_values.csv
* cagr_report.csv
* max_drawdown.csv

---

## Database Structure

SQLite Database:

```text
bluestock_mf.db
```

The database contains cleaned and validated mutual fund datasets used for analytics and dashboard reporting.

Supporting SQL files:

```text
sql/schema.sql
sql/queries.sql
```

---

## ETL Workflow

### Extract

* Load raw CSV files
* Validate data integrity
* Fetch live NAV data

Scripts:

```text
scripts/data_ingestion.py
scripts/live_nav_fetch.py
scripts/amfi_validation.py
```

### Transform

* Clean missing values
* Standardize formats
* Remove duplicates
* Validate financial metrics

Scripts:

```text
scripts/clean_nav_history.py
scripts/clean_transactions.py
scripts/clean_perfomance.py
scripts/clean_remaining_datasets.py
```

### Load

* Store processed datasets into SQLite

Script:

```text
scripts/load_sqlite.py
```

---

## Exploratory Data Analysis

The project includes comprehensive EDA covering:

* AUM growth analysis
* SIP inflow trends
* Folio growth analysis
* State-wise investment distribution
* Sector allocation analysis
* Risk grade distribution
* Expense ratio analysis
* Gender and city-tier segmentation
* Correlation analysis

Notebook:

```text
notebooks/EDA_Analysis.ipynb
```

---

## Performance Analytics

Advanced fund performance metrics include:

* CAGR
* Alpha
* Beta
* Sharpe Ratio
* Sortino Ratio
* Maximum Drawdown
* Benchmark Comparison

Notebook:

```text
notebooks/Perfomance_Analytics.ipynb
```

Generated Outputs:

```text
fund_scorecard.csv
alpha_beta.csv
benchmark_comparison.png
```

---

## Advanced Analytics

Additional analytics performed:

* Value at Risk (VaR)
* Conditional VaR (CVaR)
* SIP Continuity Analysis
* Sector Concentration Analysis
* Fund Recommendation Engine

Notebook:

```text
notebooks/Advanced_Analytics.ipynb
```

Key Outputs:

```text
var_cvar_report.csv
sip_continuity.csv
sector_hhi.csv
recommender.py
```

---

## Power BI Dashboard

The Power BI dashboard contains four interactive pages:

### Page 1 – Industry Overview

* Total AUM KPI
* SIP Inflows KPI
* Total Folios KPI
* Total Schemes KPI
* Industry AUM Trend
* Top 10 Fund Houses by AUM

### Page 2 – Fund Performance Analytics

* Return vs Risk Scatter Plot
* NAV vs Benchmark Comparison
* Fund Scorecard Table
* Interactive Fund Filters

### Page 3 – Investor Analytics

* Transaction Amount by State
* Transaction Type Distribution
* Average SIP by Age Group
* Monthly Transaction Volume

### Page 4 – SIP & Market Trends

* SIP Inflows vs Nifty50
* Category Inflow Heatmap
* Top Categories by Net Inflow
* SIP Growth KPI

---

## Folder Structure

```text
BLUESTOCK_MF_CAPSTONE
│
├── charts/
├── dashboard/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── reports/
├── scripts/
├── sql/
│
├── bluestock_mf.db
├── README.md
└── run_pipeline.py
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd BLUESTOCK_MF_CAPSTONE
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the ETL pipeline:

```bash
python run_pipeline.py
```

Open the Power BI dashboard:

```text
dashboard/bluestock_mf_dashboard.pbix
```

---

## Dashboard Screenshots

Add the following screenshots:

* Industry Overview
* Fund Performance Analytics
* Investor Analytics
* SIP & Market Trends

---

## Key Insights

* Mutual fund industry AUM demonstrated strong growth from 2022–2025.
* SIP participation increased consistently over the analysis period.
* Large-cap and liquid categories contributed significantly to inflows.
* Fund performance varied considerably across categories and risk profiles.
* Investor activity exhibited meaningful regional and demographic patterns.

---

## Future Improvements

* Real-time market data integration
* Automated dashboard refresh
* Predictive return forecasting
* Portfolio optimization models
* Cloud deployment
* Power BI Service integration

---

## Author

**Vani Arya**

Bluestock Fintech Internship Program

Mutual Fund Analytics Capstone Project

2026

---

## License

This project was developed for educational and internship evaluation purposes.
