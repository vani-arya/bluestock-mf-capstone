import pandas as pd

# Load scheme performance data
df = pd.read_csv(
    "../data/processed/07_scheme_performance_clean.csv"
)

# User input
risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

# Filter by risk grade
filtered = df[
    df['risk_grade'].str.lower()
    ==
    risk.lower()
]

# Top 3 funds by Sharpe Ratio
recommendations = (
    filtered
    .sort_values(
        'sharpe_ratio',
        ascending=False
    )
    .head(3)
)

print("\nTop 3 Recommended Funds:\n")

print(
    recommendations[
        [
            'scheme_name',
            'risk_grade',
            'sharpe_ratio'
        ]
    ]
)