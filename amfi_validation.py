import pandas as pd

master = pd.read_csv("data/raw/fund_master.csv")
nav = pd.read_csv("data/raw/nav_history.csv")

master_codes = set(master["scheme_code"])
nav_codes = set(nav["scheme_code"])

missing_codes = master_codes - nav_codes

print("Missing Codes:", len(missing_codes))
print(missing_codes)
