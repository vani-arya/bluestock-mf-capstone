# Day 1 Data Quality Report

## Dataset Loading Summary

- Successfully loaded all 10 provided CSV datasets.
- No file loading errors encountered.

## Initial Observations

1. Date columns in multiple datasets are currently stored as string type and will require datetime conversion during data cleaning.
2. NAV history dataset contains approximately 46,000 records and is the largest dataset.
3. Investor transaction dataset contains approximately 32,000 records and appears suitable for transaction analysis.
4. Financial metrics such as NAV, Alpha, Beta, Sharpe Ratio and Expense Ratio have been loaded with appropriate numeric data types.
5. Initial null values were observed in the `yoy_growth_pct` column of the SIP inflow dataset, which is expected due to unavailable prior-year data.

## Conclusion

All datasets were successfully ingested and appear structurally sound. No critical data quality issues were identified during the initial inspection. Further validation and cleaning will be performed during Day 2.

## Fund Master Analysis

Fund Houses Identified:
- SBI Mutual Fund
- HDFC Mutual Fund
- ICICI Prudential MF
- Nippon India MF
- Kotak Mahindra MF

Categories Found:
- Equity
- Debt
- Hybrid

Risk Categories Found:
- Low
- Moderate
- High
- Very High

## AMFI Validation

Validation was performed between:

- 01_fund_master.csv
- 02_nav_history.csv

Result:

All AMFI codes present in the master dataset were found in the NAV history dataset.

No missing scheme codes detected.