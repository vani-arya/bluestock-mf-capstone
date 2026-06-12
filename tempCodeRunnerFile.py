import pandas as pd

nav = pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
)

print(
    nav["amfi_code"].nunique()
)