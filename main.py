
from extract.extract_data import (
    generate_products,
    generate_customers,
    generate_transactions
)

from transform.transform_data import transform_data
from load.load_data import load_to_postgres

def run_pipeline():
    print("Starting ETL Pipeline...")

    generate_products()
    generate_customers()
    generate_transactions()

    transform_data()

    load_to_postgres()

    print("ETL Pipeline Completed Successfully.")


if __name__ == "__main__":
    run_pipeline()
