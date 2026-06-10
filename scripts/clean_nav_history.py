import pandas as pd

df = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

print("Original Rows:", len(df))

# Convert date

df["date"] = pd.to_datetime(
    df["date"]
)

# Sort

df = df.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates

df = df.drop_duplicates()

# Forward fill NAV

df["nav"] = (
    df.groupby("amfi_code")
    ["nav"]
    .ffill()
)

# Check invalid NAV

invalid = df[df["nav"] <= 0]

print(
    "Invalid NAV:",
    len(invalid)
)

df.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("Saved")