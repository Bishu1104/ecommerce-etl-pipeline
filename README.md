
# E-Commerce ETL Pipeline (Python)

## Project Overview
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline for e-commerce analytics.

### Features
- Extract product, customer, and transaction data
- Transform and clean raw datasets
- Load cleaned data into PostgreSQL
- Logging and modular architecture
- Ready for scheduling with Airflow or Cron

---

## Tech Stack
- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- Faker
- Logging

---

## Project Structure

ecommerce_etl_pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── extract/
│   └── extract_data.py
│
├── transform/
│   └── transform_data.py
│
├── load/
│   └── load_data.py
│
├── config/
│   └── config.py
│
├── logs/
│
├── main.py
├── requirements.txt
└── schema.sql

---

## Run Pipeline

### Install dependencies
pip install -r requirements.txt

### Create PostgreSQL database
CREATE DATABASE ecommerce_db;

### Run schema
Execute schema.sql in PostgreSQL.

### Run ETL
python main.py
