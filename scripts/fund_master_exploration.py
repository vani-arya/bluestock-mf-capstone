import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

print("="*50)
print("FUND HOUSES")
print("="*50)
print(df["fund_house"].unique())

print("\n")

print("="*50)
print("CATEGORIES")
print("="*50)
print(df["category"].unique())

print("\n")

print("="*50)
print("SUB CATEGORIES")
print("="*50)
print(df["sub_category"].unique())

print("\n")

print("="*50)
print("RISK CATEGORIES")
print("="*50)
print(df["risk_category"].unique())