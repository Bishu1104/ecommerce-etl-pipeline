
CREATE TABLE ecommerce_transactions (
    transaction_id INT,
    customer_id INT,
    product_id INT,
    quantity INT,
    payment_method VARCHAR(50),
    product_name VARCHAR(255),
    category VARCHAR(100),
    price NUMERIC,
    customer_name VARCHAR(255),
    email VARCHAR(255),
    city VARCHAR(255),
    total_amount NUMERIC
);
