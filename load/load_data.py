import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

PROCESSED_PATH = Path("data/processed")

def load_to_postgres():
    df = pd.read_csv(PROCESSED_PATH / "final_data.csv")

    db_url = "postgresql://postgres:password@localhost:5432/ecommerce_db"

    engine = create_engine(db_url)

    df.to_sql(
        "ecommerce_transactions",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded into PostgreSQL successfully.")

if __name__ == "__main__":
    load_to_postgres()
