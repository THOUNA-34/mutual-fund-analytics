# 📈 Mutual Fund Analytics Dashboard

> A comprehensive Mutual Fund Analytics Platform for analyzing NAV trends, returns, risk metrics, fund performance, and investment insights using Python, SQL, and Interactive Dashboards.

---

## 🎯 Project Objective

The goal of this project is to build an end-to-end Mutual Fund Analytics System that:

* Ingests and validates mutual fund datasets
* Fetches live NAV data from MFAPI
* Performs return and risk analysis
* Calculates CAGR and rolling returns
* Compares mutual fund performance
* Generates interactive dashboards
* Provides actionable investment insights

---

## 🚀 Key Features

### 📥 Data Ingestion

* Load multiple mutual fund datasets
* Automated validation checks
* Missing value detection
* Duplicate record identification

### 🌐 Live NAV Tracking

* Real-time NAV fetching using MFAPI
* Historical NAV collection
* Fund-wise NAV storage

### 📊 Performance Analytics

* CAGR Analysis
* Absolute Returns
* Rolling Returns
* SIP Return Analysis

### ⚠️ Risk Analytics

* Standard Deviation
* Sharpe Ratio
* Sortino Ratio
* Beta Analysis
* Volatility Comparison

### 📈 Dashboard & Visualization

* Interactive Plotly Charts
* NAV Trend Analysis
* Fund Comparison Dashboard
* Risk vs Return Visualizations

---

## 🏗️ Project Architecture

```text
mutual_fund_analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── sql/
│
├── dashboard/
│
├── reports/
│
├── data_ingestion.py
├── live_nav_fetch.py
├── fetch_top_funds.py
├── fund_master_explore.py
├── amfi_validation.py
├── data_quality_report.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Tech Stack

| Category             | Technologies                |
| -------------------- | --------------------------- |
| Programming          | Python                      |
| Data Analysis        | Pandas, NumPy               |
| Visualization        | Matplotlib, Seaborn, Plotly |
| Statistical Analysis | SciPy                       |
| Database             | SQLAlchemy                  |
| API Integration      | Requests                    |
| Development          | Jupyter Notebook            |
| Version Control      | Git & GitHub                |

---

## 📂 Datasets Used

Current Development Datasets:

* fund_master.csv
* nav_history.csv
* scheme_aum.csv
* category_master.csv
* expense_ratio.csv
* benchmark_returns.csv
* risk_metrics.csv
* fund_manager.csv
* amfi_codes.csv
* scheme_returns.csv

---

## 🌐 Data Source

Live NAV data is fetched from:

https://api.mfapi.in

---

## 📅 Development Roadmap

### ✅ Day 1 – Data Ingestion

* Project setup
* Dataset loading
* Data validation
* AMFI code verification
* Live NAV fetching
* Data quality report generation

### 🔄 Day 2 – Data Cleaning

* Missing value handling
* Data standardization
* Date conversion
* Processed dataset generation

### 📊 Day 3 – Return Analytics

* CAGR calculations
* Rolling returns
* Fund performance comparisons
* SIP analysis

### 📉 Day 4 – Risk Analytics

* Sharpe Ratio
* Sortino Ratio
* Beta Calculation
* Volatility Analysis

### 📈 Day 5 – Dashboard Development

* Plotly Interactive Dashboard
* Fund Comparison Views
* Risk vs Return Analysis
* Performance Monitoring

---

## 📸 Sample Output

### Data Quality Validation

✔ Missing Values Detection

✔ Duplicate Record Detection

✔ AMFI Scheme Validation

✔ Dataset Profiling

### Live NAV Fetching

✔ HDFC Top 100 Fund

✔ SBI Bluechip Fund

✔ ICICI Bluechip Fund

✔ Nippon Large Cap Fund

✔ Axis Bluechip Fund

✔ Kotak Bluechip Fund

---

## 🎓 Academic Context

Developed as part of a Data Analytics & Financial Intelligence project to demonstrate:

* Data Engineering
* Exploratory Data Analysis
* Financial Analytics
* Dashboard Development
* Python Automation
* API Integration

---

## 👨‍💻 Author

**Thouna Khaidem**

B.E. Artificial Intelligence & Data Science

East Point College of Engineering & Technology

GitHub: https://github.com/THOUNA-34

---

⭐ If you find this project useful, consider giving it a star.
