--1
SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

--2
SELECT
state,
SUM(amount_inr)
FROM fact_transactions
GROUP BY state;

--3
SELECT
    scheme_name,
    return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;

--4
SELECT
    category,
    AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance
GROUP BY category;

--5
SELECT
    transaction_type,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

--6
SELECT
    state,
    COUNT(DISTINCT investor_id) AS investor_count
FROM fact_transactions
GROUP BY state
ORDER BY investor_count DESC;

--7
SELECT
    amfi_code,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY average_nav DESC;

--8
SELECT
    state,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 5;

--9
SELECT
    risk_category,
    COUNT(*) AS fund_count
FROM dim_fund
GROUP BY risk_category;

--10
SELECT
    category,
    SUM(net_inflow_crore) AS total_inflow
FROM category_inflows
GROUP BY category
ORDER BY total_inflow DESC;


--1. Top 5 Funds by AUM
--2. Average NAV per Month
--3. SIP YoY Growth
--4. Transactions by State
--5. Funds with Expense Ratio < 1%
--6. Top 10 Funds by 1-Year Return
--7. Average Expense Ratio by Category
--8. Total Investment Amount by Transaction Type
--9. Number of Investors by State
--10. Top 5 States by Investment Amount