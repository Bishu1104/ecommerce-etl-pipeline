# E-Commerce ETL Pipeline

A production-ready ETL pipeline built using Python, PostgreSQL, Docker, and GitHub Actions.

## Features

- Extract product, customer, and transaction data
- Transform raw datasets into analytics-ready format
- Load processed data into PostgreSQL
- Dockerized architecture
- Automated CI/CD pipeline using GitHub Actions
- Modular and scalable ETL structure

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Docker
- GitHub Actions

## Project Structure

```bash
ecommerce-etl-pipeline/
│
├── extract/
├── transform/
├── load/
├── config/
├── tests/
├── .github/workflows/
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md
```

## CI/CD Workflow

- Automatically triggers on every push
- Installs dependencies
- Runs workflow validation
- Builds Docker image

## Future Improvements

- Apache Airflow orchestration
- AWS deployment
- Real API integration
- Power BI dashboard
- Data quality monitoring
