#08_investor_transactions.csv

import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Date

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardize type

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.upper()
)

# Check amount

bad_amount = df[
    df["amount_inr"] <= 0
]

print(
    "Invalid Amount:",
    len(bad_amount)
)

print(
    df["kyc_status"].unique()
)

df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("Saved")