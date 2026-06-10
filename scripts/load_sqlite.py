import pandas as pd

from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

files = {

"dim_fund":
"01_fund_master_clean.csv",

"fact_nav":
"02_nav_history_clean.csv",

"fact_aum":
"03_aum_by_fund_house_clean.csv",

"fact_performance":
"07_scheme_performance_clean.csv",

"fact_transactions":
"08_investor_transactions_clean.csv"

}

for table, file in files.items():

    df = pd.read_csv(
        f"data/processed/{file}"
    )

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"Loaded {table}"
    )