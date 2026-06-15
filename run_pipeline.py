"""
Master execution pipeline for Mutual Fund Analytics Capstone
"""

import subprocess

scripts = [
    "scripts/data_ingestion.py",
    "scripts/load_sqlite.py",
    "scripts/clean_nav_history.py",
    "scripts/clean_transactions.py",
    "scripts/clean_perfomance.py",
    "scripts/clean_remaining_datasets.py"
]

for script in scripts:
    print(f"Running {script}")
    subprocess.run(["python", script], check=True)

print("Pipeline completed successfully.")