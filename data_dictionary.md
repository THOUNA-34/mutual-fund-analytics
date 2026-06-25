# Data Dictionary

## Project

**Mutual Fund Analytics Dashboard**

---

# 1. fund_master

| Column      | Data Type | Description                    | Source      |
| ----------- | --------- | ------------------------------ | ----------- |
| amfi_code   | INTEGER   | Unique AMFI scheme identifier  | AMFI        |
| scheme_name | TEXT      | Mutual fund scheme name        | Fund Master |
| fund_house  | TEXT      | Asset Management Company       | Fund Master |
| category    | TEXT      | Fund category                  | Fund Master |
| subcategory | TEXT      | Fund subcategory               | Fund Master |
| risk_grade  | TEXT      | Investment risk classification | Fund Master |

---

# 2. nav_history

| Column    | Data Type | Description            | Source |
| --------- | --------- | ---------------------- | ------ |
| amfi_code | INTEGER   | Mutual fund identifier | MFAPI  |
| date      | DATE      | NAV date               | MFAPI  |
| nav       | REAL      | Net Asset Value        | MFAPI  |

---

# 3. investor_transactions

| Column           | Data Type | Description                   | Source       |
| ---------------- | --------- | ----------------------------- | ------------ |
| transaction_id   | INTEGER   | Unique transaction identifier | Transactions |
| amfi_code        | INTEGER   | Mutual fund identifier        | Transactions |
| transaction_date | DATE      | Date of transaction           | Transactions |
| transaction_type | TEXT      | SIP / Lumpsum / Redemption    | Transactions |
| amount           | REAL      | Transaction amount            | Transactions |
| state            | TEXT      | Investor state                | Transactions |
| kyc_status       | TEXT      | KYC verification status       | Transactions |

---

# 4. scheme_performance

| Column        | Data Type | Description                         | Source      |
| ------------- | --------- | ----------------------------------- | ----------- |
| amfi_code     | INTEGER   | Mutual fund identifier              | Performance |
| return_1y     | REAL      | One-year return (%)                 | Performance |
| return_3y     | REAL      | Three-year return (%)               | Performance |
| return_5y     | REAL      | Five-year return (%)                | Performance |
| expense_ratio | REAL      | Annual expense ratio (%)            | Performance |
| anomaly       | BOOLEAN   | Indicates invalid or missing values | Generated   |

---

# 5. scheme_aum

| Column    | Data Type | Description                       | Source |
| --------- | --------- | --------------------------------- | ------ |
| amfi_code | INTEGER   | Mutual fund identifier            | AUM    |
| aum_cr    | REAL      | Assets Under Management (₹ Crore) | AUM    |

---

# 6. category_master

| Column      | Data Type | Description          | Source          |
| ----------- | --------- | -------------------- | --------------- |
| category    | TEXT      | Category name        | Category Master |
| description | TEXT      | Category description | Category Master |

---

# 7. expense_ratio

| Column        | Data Type | Description            | Source        |
| ------------- | --------- | ---------------------- | ------------- |
| amfi_code     | INTEGER   | Mutual fund identifier | Expense Ratio |
| expense_ratio | REAL      | Expense ratio (%)      | Expense Ratio |

---

# 8. benchmark_returns

| Column    | Data Type | Description                   | Source    |
| --------- | --------- | ----------------------------- | --------- |
| benchmark | TEXT      | Benchmark index               | Benchmark |
| return_1y | REAL      | One-year benchmark return (%) | Benchmark |

---

# 9. risk_metrics

| Column    | Data Type | Description            | Source       |
| --------- | --------- | ---------------------- | ------------ |
| amfi_code | INTEGER   | Mutual fund identifier | Risk Metrics |
| beta      | REAL      | Beta value             | Risk Metrics |
| sharpe    | REAL      | Sharpe Ratio           | Risk Metrics |

---

# 10. fund_manager

| Column    | Data Type | Description            | Source       |
| --------- | --------- | ---------------------- | ------------ |
| amfi_code | INTEGER   | Mutual fund identifier | Fund Manager |
| manager   | TEXT      | Name of fund manager   | Fund Manager |

---

# 11. amfi_codes

| Column    | Data Type | Description                          | Source |
| --------- | --------- | ------------------------------------ | ------ |
| amfi_code | INTEGER   | Official AMFI registered scheme code | AMFI   |

---

# Business Rules

* AMFI codes must be unique.
* NAV values must always be greater than zero.
* Transaction amounts must be positive.
* Expense ratios must be between **0.1% and 2.5%**.
* KYC status must be one of:

  * Verified
  * Pending
  * Rejected
* Transaction types are standardized to:

  * SIP
  * Lumpsum
  * Redemption

---

# Data Sources

* MFAPI
* AMFI
* Fund Master Dataset
* Investor Transaction Dataset
* Scheme Performance Dataset
* Benchmark Returns Dataset
* Risk Metrics Dataset
