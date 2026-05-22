import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")
PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

def transform_data():
    products = pd.read_csv(RAW_PATH / "products.csv")
    customers = pd.read_csv(RAW_PATH / "customers.csv")
    transactions = pd.read_csv(RAW_PATH / "transactions.csv")

    merged_df = transactions.merge(products, on="product_id")
    merged_df = merged_df.merge(customers, on="customer_id")

    merged_df["total_amount"] = merged_df["quantity"] * merged_df["price"]

    merged_df.to_csv(PROCESSED_PATH / "final_data.csv", index=False)

    print("Transformation completed successfully.")

if __name__ == "__main__":
    transform_data()
