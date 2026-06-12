import pandas as pd
import os

folder = "data/processed"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)

        try:
            df = pd.read_csv(path)

            print("\n" + "="*50)
            print(file)
            print(df.columns.tolist())

        except Exception as e:
            print(file, e)

