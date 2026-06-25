-- ==========================================================
-- DIMENSION TABLES
-- ==========================================================

CREATE TABLE dim_fund (

    fund_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER UNIQUE,

    scheme_name TEXT,

    fund_house TEXT,

    category TEXT,

    subcategory TEXT,

    risk_grade TEXT

);

CREATE TABLE dim_date (

    date_id INTEGER PRIMARY KEY AUTOINCREMENT,

    full_date DATE UNIQUE,

    year INTEGER,

    month INTEGER,

    day INTEGER,

    quarter INTEGER

);

-- ==========================================================
-- FACT TABLES
-- ==========================================================

CREATE TABLE fact_nav (

    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER,

    date_id INTEGER,

    nav REAL,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)

);

CREATE TABLE fact_transactions (

    transaction_id INTEGER PRIMARY KEY,

    fund_id INTEGER,

    date_id INTEGER,

    transaction_type TEXT,

    amount REAL,

    state TEXT,

    kyc_status TEXT,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)

);

CREATE TABLE fact_performance (

    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER,

    return_1y REAL,

    return_3y REAL,

    return_5y REAL,

    expense_ratio REAL,

    anomaly BOOLEAN,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id)

);

CREATE TABLE fact_aum (

    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER,

    aum_cr REAL,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id)

);