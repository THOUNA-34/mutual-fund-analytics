import shutil
from pathlib import Path

import pandas as pd

# ==============================================================================
# BLUESTOCK MUTUAL FUND ANALYTICS
# DAY 2 - DATA CLEANING
# ==============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 80)
print("BLUESTOCK MUTUAL FUND ANALYTICS")
print("DAY 2 - DATA CLEANING")
print("=" * 80)

print(f"\nRaw Directory      : {RAW_DIR}")
print(f"Processed Directory: {PROCESSED_DIR}")

# ==============================================================================
# CLEAN NAV HISTORY
# ==============================================================================

print("\n" + "=" * 80)
print("Cleaning nav_history.csv")
print("=" * 80)

nav = pd.read_csv(RAW_DIR / "nav_history.csv")

print(f"Original Rows : {len(nav)}")

# Convert date
nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

# Remove invalid dates
nav = nav.dropna(subset=["date"])

# Sort
nav = nav.sort_values(
    by=["amfi_code", "date"]
)

# Forward fill NAV
nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
    .ffill()
)

# Remove duplicates
duplicates = nav.duplicated().sum()

print(f"Duplicate Rows : {duplicates}")

nav = nav.drop_duplicates()

# Validate NAV
invalid_nav = (nav["nav"] <= 0).sum()

print(f"Invalid NAV : {invalid_nav}")

nav = nav[
    nav["nav"] > 0
]

nav.to_csv(
    PROCESSED_DIR / "nav_history.csv",
    index=False
)

print(f"Cleaned Rows : {len(nav)}")
print("✓ nav_history.csv cleaned successfully")

# ==============================================================================
# CLEAN INVESTOR TRANSACTIONS
# ==============================================================================

print("\n" + "=" * 80)
print("Cleaning investor_transactions.csv")
print("=" * 80)

transactions = pd.read_csv(
    RAW_DIR / "investor_transactions.csv"
)

print(f"Original Rows : {len(transactions)}")

# Standardize transaction type
transactions["transaction_type"] = (
    transactions["transaction_type"]
    .astype(str)
    .str.strip()
    .str.upper()
)

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .replace({
        "SIP": "SIP",
        "LUMPSUM": "Lumpsum",
        "REDEMPTION": "Redemption"
    })
)

print("\nTransaction Types")

print(
    transactions["transaction_type"].value_counts()
)

# Date conversion
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"],
    errors="coerce",
    dayfirst=True
)

invalid_dates = (
    transactions["transaction_date"]
    .isna()
    .sum()
)

print(f"\nInvalid Dates : {invalid_dates}")

transactions = transactions.dropna(
    subset=["transaction_date"]
)

# Validate amount
invalid_amount = (
    transactions["amount"] <= 0
).sum()

print(f"Invalid Amounts : {invalid_amount}")

transactions = transactions[
    transactions["amount"] > 0
]

# Validate KYC
valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

invalid_kyc = (
    ~transactions["kyc_status"]
    .isin(valid_kyc)
).sum()

print(f"Invalid KYC Values : {invalid_kyc}")

transactions = transactions[
    transactions["kyc_status"]
    .isin(valid_kyc)
]

duplicates = (
    transactions
    .duplicated()
    .sum()
)

print(f"Duplicate Rows : {duplicates}")

transactions = transactions.drop_duplicates()

transactions.to_csv(
    PROCESSED_DIR / "investor_transactions.csv",
    index=False
)

print(f"Cleaned Rows : {len(transactions)}")

print("✓ investor_transactions.csv cleaned successfully")

# ==============================================================================
# CLEAN SCHEME PERFORMANCE
# ==============================================================================

print("\n" + "=" * 80)
print("Cleaning scheme_performance.csv")
print("=" * 80)

performance = pd.read_csv(
    RAW_DIR / "scheme_performance.csv"
)

print(f"Original Rows : {len(performance)}")

return_columns = [
    "return_1y",
    "return_3y",
    "return_5y"
]

for column in return_columns:

    performance[column] = pd.to_numeric(
        performance[column],
        errors="coerce"
    )

performance["anomaly"] = (
    performance[return_columns]
    .isna()
    .any(axis=1)
)

print(
    f"Anomalies Found : {performance['anomaly'].sum()}"
)

invalid_expense = (
    ~performance["expense_ratio"]
    .between(0.1, 2.5)
).sum()

print(
    f"Invalid Expense Ratios : {invalid_expense}"
)

performance = performance[
    performance["expense_ratio"]
    .between(0.1, 2.5)
]

performance.to_csv(
    PROCESSED_DIR / "scheme_performance.csv",
    index=False
)

print(f"Cleaned Rows : {len(performance)}")

print("✓ scheme_performance.csv cleaned successfully")

# ==============================================================================
# COPY REMAINING DATASETS
# ==============================================================================

print("\n" + "=" * 80)
print("Copying Remaining Datasets")
print("=" * 80)

remaining = [

    "fund_master.csv",

    "scheme_aum.csv",

    "category_master.csv",

    "expense_ratio.csv",

    "benchmark_returns.csv",

    "risk_metrics.csv",

    "fund_manager.csv",

    "amfi_codes.csv",

    "portfolio_holdings.csv",

    "sip_monthly.csv",

    "category_inflows.csv",

    "folio_growth.csv"

]

for file in remaining:

    shutil.copy(
        RAW_DIR / file,
        PROCESSED_DIR / file
    )

    print(f"Copied : {file}")

# ==============================================================================
# SUMMARY
# ==============================================================================

print("\n" + "=" * 80)
print("DATA CLEANING SUMMARY")
print("=" * 80)

print(f"NAV Records              : {len(nav)}")
print(f"Transaction Records      : {len(transactions)}")
print(f"Performance Records      : {len(performance)}")
print(f"Other Files Copied       : {len(remaining)}")

print("\nProcessed datasets saved to:")

print(PROCESSED_DIR)

print("\nDAY 2 DATA CLEANING COMPLETED SUCCESSFULLY")