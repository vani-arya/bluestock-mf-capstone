# Data Dictionary

## 01_fund_master.csv

| Column             | Data Type | Description                                     |
| ------------------ | --------- | ----------------------------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme code                         |
| fund_house         | Text      | Mutual fund company name                        |
| scheme_name        | Text      | Name of the mutual fund scheme                  |
| category           | Text      | Fund category (Equity, Debt, Hybrid, etc.)      |
| sub_category       | Text      | Specific category within the fund type          |
| plan               | Text      | Regular or Direct plan                          |
| launch_date        | Date      | Scheme launch date                              |
| benchmark          | Text      | Benchmark index used for performance comparison |
| expense_ratio_pct  | Float     | Annual expense ratio percentage                 |
| exit_load_pct      | Float     | Exit load charged on redemption                 |
| min_sip_amount     | Integer   | Minimum SIP investment amount                   |
| min_lumpsum_amount | Integer   | Minimum lump sum investment amount              |
| fund_manager       | Text      | Name of the fund manager                        |
| risk_category      | Text      | Risk classification of the scheme               |
| sebi_category_code | Text      | SEBI classification code                        |

---

## 02_nav_history.csv

| Column    | Data Type | Description                   |
| --------- | --------- | ----------------------------- |
| amfi_code | Integer   | Unique AMFI scheme code       |
| date      | Date      | NAV date                      |
| nav       | Float     | Net Asset Value of the scheme |

---

## 03_aum_by_fund_house.csv

| Column         | Data Type | Description                            |
| -------------- | --------- | -------------------------------------- |
| date           | Date      | Reporting date                         |
| fund_house     | Text      | Mutual fund company                    |
| aum_lakh_crore | Float     | Assets Under Management in lakh crores |
| aum_crore      | Integer   | Assets Under Management in crores      |
| num_schemes    | Integer   | Number of schemes managed              |

---

## 04_monthly_sip_inflows.csv

| Column                    | Data Type | Description                               |
| ------------------------- | --------- | ----------------------------------------- |
| month                     | Date      | Reporting month                           |
| sip_inflow_crore          | Integer   | Monthly SIP inflow amount in crores       |
| active_sip_accounts_crore | Float     | Number of active SIP accounts (crores)    |
| new_sip_accounts_lakh     | Float     | New SIP accounts opened (lakhs)           |
| sip_aum_lakh_crore        | Float     | SIP Assets Under Management (lakh crores) |
| yoy_growth_pct            | Float     | Year-over-year growth percentage          |

---

## 05_category_inflows.csv

| Column           | Data Type | Description                 |
| ---------------- | --------- | --------------------------- |
| month            | Date      | Reporting month             |
| category         | Text      | Mutual fund category        |
| net_inflow_crore | Float     | Net inflow amount in crores |

---

## 06_industry_folio_count.csv

| Column              | Data Type | Description                     |
| ------------------- | --------- | ------------------------------- |
| month               | Date      | Reporting month                 |
| total_folios_crore  | Float     | Total investor folios in crores |
| equity_folios_crore | Float     | Equity fund folios in crores    |
| debt_folios_crore   | Float     | Debt fund folios in crores      |
| hybrid_folios_crore | Float     | Hybrid fund folios in crores    |
| others_folios_crore | Float     | Other fund folios in crores     |

---

## 07_scheme_performance.csv

| Column             | Data Type | Description                               |
| ------------------ | --------- | ----------------------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme code                   |
| scheme_name        | Text      | Mutual fund scheme name                   |
| fund_house         | Text      | Mutual fund company                       |
| category           | Text      | Fund category                             |
| plan               | Text      | Direct or Regular plan                    |
| return_1yr_pct     | Float     | One-year return percentage                |
| return_3yr_pct     | Float     | Three-year return percentage              |
| return_5yr_pct     | Float     | Five-year return percentage               |
| benchmark_3yr_pct  | Float     | Three-year benchmark return               |
| alpha              | Float     | Fund perfomance compared to benchmark     |
| beta               | Float     | Fund violation campared to market         |
| sharpe_ratio       | Float     | Risk-adjusted performance ratio           |
| sortino_ratio      | Float     | Perfomance considering downside risk      |
| std_dev_ann_pct    | Float     | Annualized standard deviation             |
| max_drawdown_pct   | Float     | Maximum portfolio decline                 |
| aum_crore          | Integer   | Assets Under Management in crores         |
| expense_ratio_pct  | Float     | Annual expense ratio                      |
| morningstar_rating | Integer   | Morningstar rating                        |
| risk_grade         | Text      | Risk classification                       |

---

## 08_investor_transactions.csv

| Column             | Data Type | Description                 |
| ------------------ | --------- | --------------------------- |
| investor_id        | Text      | Unique investor identifier  |
| transaction_date   | Date      | Transaction date            |
| amfi_code          | Integer   | AMFI scheme code            |
| transaction_type   | Text      | SIP, Lumpsum, or Redemption |
| amount_inr         | Integer   | Transaction amount in INR   |
| state              | Text      | Investor state              |
| city               | Text      | Investor city               |
| city_tier          | Text      | Tier classification of city |
| age_group          | Text      | Investor age group          |
| gender             | Text      | Investor gender             |
| annual_income_lakh | Float     | Annual income in lakhs      |
| payment_mode       | Text      | Mode of payment             |
| kyc_status         | Text      | KYC verification status     |

---

## 09_portfolio_holdings.csv

| Column            | Data Type | Description                     |
| ----------------- | --------- | ------------------------------- |
| amfi_code         | Integer   | AMFI scheme code                |
| stock_symbol      | Text      | Stock market symbol             |
| stock_name        | Text      | Company name                    |
| sector            | Text      | Industry sector                 |
| weight_pct        | Float     | Portfolio allocation percentage |
| market_value_cr   | Float     | Market value in crores          |
| current_price_inr | Float     | Current stock price             |
| portfolio_date    | Date      | Portfolio reporting date        |

---

## 10_benchmark_indices.csv

| Column      | Data Type | Description          |
| ----------- | --------- | -------------------- |
| date        | Date      | Trading date         |
| index_name  | Text      | Benchmark index name |
| close_value | Float     | Closing index value  |

## Source References

* Mutual Fund Master Data
* Historical NAV Records
* AUM Reports
* SIP Industry Reports
* Category-wise Inflow Reports
* Folio Statistics
* Scheme Performance Metrics
* Investor Transaction Records
* Portfolio Holdings Data
* Benchmark Index Historical Data
