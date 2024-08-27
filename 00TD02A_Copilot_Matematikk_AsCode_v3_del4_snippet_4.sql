CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    product_id INT,
    product_name VARCHAR(255),
    quantity INT,
    order_date DATE
);