import pandas as pd
import os

DATA_PATH = "data/raw"

files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

print("=" * 80)
print("DATA INGESTION REPORT")
print("=" * 80)

for file in files:
    path = os.path.join(DATA_PATH, file)

    print("\n" + "=" * 80)
    print(f"FILE: {file}")
    print("=" * 80)

    try:
        df = pd.read_csv(path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}: {e}")
