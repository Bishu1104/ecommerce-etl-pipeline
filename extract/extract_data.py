import pandas as pd
from faker import Faker
import random
from pathlib import Path

fake = Faker()

RAW_PATH = Path("data/raw")
RAW_PATH.mkdir(parents=True, exist_ok=True)

def generate_products(n=50):
    products = []
    for i in range(n):
        products.append({
            "product_id": i + 1,
            "product_name": fake.word(),
            "category": random.choice(["Electronics", "Fashion", "Home", "Sports"]),
            "price": round(random.uniform(10, 1000), 2)
        })

    df = pd.DataFrame(products)
    df.to_csv(RAW_PATH / "products.csv", index=False)

def generate_customers(n=100):
    customers = []
    for i in range(n):
        customers.append({
            "customer_id": i + 1,
            "customer_name": fake.name(),
            "email": fake.email(),
            "city": fake.city()
        })

    df = pd.DataFrame(customers)
    df.to_csv(RAW_PATH / "customers.csv", index=False)

def generate_transactions(n=200):
    transactions = []
    for i in range(n):
        transactions.append({
            "transaction_id": i + 1,
            "customer_id": random.randint(1, 100),
            "product_id": random.randint(1, 50),
            "quantity": random.randint(1, 5),
            "payment_method": random.choice(["UPI", "Card", "NetBanking"])
        })

    df = pd.DataFrame(transactions)
    df.to_csv(RAW_PATH / "transactions.csv", index=False)

if __name__ == "__main__":
    generate_products()
    generate_customers()
    generate_transactions()

    print("Raw data generated successfully.")
