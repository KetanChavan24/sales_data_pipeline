# Retail Sales ETL Pipeline

## Business Problem

A retail company receives daily sales data as CSV exports from multiple stores. Before this data can be used for reporting and analytics, it must be cleaned, validated, and stored in a centralized database.

Since real-world datasets are often inconsistent and contain errors, this project simulates a realistic production scenario by generating a messy dataset instead of using a polished public dataset.

---

## Dataset

The dataset is **generated within the project** to closely resemble real-world retail sales data.

The generated data intentionally includes common data quality issues such as:

- Missing values
- Duplicate orders
- Invalid dates
- Negative quantities
- Incorrect prices
- Multiple date formats
- Empty rows
- Unnecessary/extra columns

These imperfections help simulate the challenges commonly faced in production ETL pipelines.

---

## Project Objective

Build an end-to-end ETL pipeline in Python that:

- Extracts sales data from CSV files
- Validates incoming records
- Cleans and transforms the data
- Loads the cleaned data into PostgreSQL
- Generates detailed execution logs
- Produces a summary report of the ETL process

---

## ETL Workflow

```text
Generated CSV
      │
      ▼
Extract Data
      │
      ▼
Validate Records
      │
      ▼
Clean & Transform Data
      │
      ▼
Load into PostgreSQL
      │
      ▼
Execution Logs + Summary Report
```

---

## Expected Output

After the pipeline execution:

- ✅ Clean sales data stored in PostgreSQL
- ✅ Invalid records identified and handled
- ✅ Duplicate records removed
- ✅ Missing values processed
- ✅ Execution logs generated
- ✅ ETL summary report created

---

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy / psycopg2
- Logging
