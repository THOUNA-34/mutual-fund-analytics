from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

# ==============================================================================
# BLUESTOCK MUTUAL FUND ANALYTICS
# DAY 2 - LOAD SQLITE DATABASE
# ==============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATABASE = PROJECT_ROOT / "bluestock_mf.db"

PROCESSED = PROJECT_ROOT / "data" / "processed"

print("=" * 80)
print("LOADING CLEANED DATASETS INTO SQLITE")
print("=" * 80)

engine = create_engine(
    f"sqlite:///{DATABASE}"
)

datasets = {

    "fund_master":
        "fund_master.csv",

    "nav_history":
        "nav_history.csv",

    "investor_transactions":
        "investor_transactions.csv",

    "scheme_performance":
        "scheme_performance.csv",

    "scheme_aum":
        "scheme_aum.csv",

    "category_master":
        "category_master.csv",

    "expense_ratio":
        "expense_ratio.csv",

    "benchmark_returns":
        "benchmark_returns.csv",

    "risk_metrics":
        "risk_metrics.csv",

    "fund_manager":
        "fund_manager.csv",

    "amfi_codes":
        "amfi_codes.csv"

}

print()

for table, file in datasets.items():

    print("-" * 70)

    print(f"Loading {file}")

    df = pd.read_csv(
        PROCESSED / file
    )

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    count = pd.read_sql(
        f"SELECT COUNT(*) AS total FROM {table}",
        engine
    )

    print(
        f"Rows Loaded : {count.iloc[0,0]}"
    )

print("\n" + "=" * 80)

print("ALL DATASETS LOADED SUCCESSFULLY")

print("=" * 80)