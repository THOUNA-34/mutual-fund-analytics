import pandas as pd

master = pd.read_csv("data/raw/fund_master.csv")
nav = pd.read_csv("data/raw/nav_history.csv")

master_codes = set(master["scheme_code"])
nav_codes = set(nav["scheme_code"])

missing_codes = master_codes - nav_codes

report = f"""
DAY 1 DATA QUALITY REPORT
=========================

DATASET SUMMARY
---------------
Total Funds                : {len(master)}
Unique Fund Houses         : {master['fund_house'].nunique()}
Unique Categories          : {master['category'].nunique()}
Unique Subcategories       : {master['subcategory'].nunique()}
Unique Risk Grades         : {master['risk_grade'].nunique()}

SCHEME CODE VALIDATION
----------------------
Total Scheme Codes (Master): {len(master_codes)}
Total Scheme Codes (NAV)   : {len(nav_codes)}
Missing Scheme Codes       : {len(missing_codes)}

MISSING VALUES
--------------
Fund House Missing         : {master['fund_house'].isnull().sum()}
Category Missing           : {master['category'].isnull().sum()}
Subcategory Missing        : {master['subcategory'].isnull().sum()}
Risk Grade Missing         : {master['risk_grade'].isnull().sum()}

DUPLICATES
----------
Duplicate Scheme Codes     : {master['scheme_code'].duplicated().sum()}

OVERALL ASSESSMENT
------------------
The ingestion process completed successfully.
All datasets were loaded into Pandas and validated.
AMFI scheme code matching was performed between fund_master and nav_history.
Further cleaning and transformation will be performed in Day 2.

END OF REPORT
"""

with open(
    "reports/day1_data_quality.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(report)

print("Report generated successfully.")
