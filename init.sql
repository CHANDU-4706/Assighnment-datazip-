CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    product_name VARCHAR(100),
    quantity INT,
    order_date DATE,
    total_amount DECIMAL(10,2)
);

INSERT INTO orders (order_id, customer_name, product_name, quantity, order_date, total_amount) VALUES
(1, 'John Doe', 'Laptop', 1, '2024-04-01', 999.99),
(2, 'Jane Smith', 'Smartphone', 2, '2024-04-02', 1599.98),
(3, 'Bob Johnson', 'Headphones', 3, '2024-04-03', 299.97),
(4, 'Alice Brown', 'Monitor', 1, '2024-04-04', 349.99),
(5, 'Charlie Wilson', 'Keyboard', 2, '2024-04-05', 159.98),
(6, 'Diana Miller', 'Mouse', 4, '2024-04-06', 119.96),
(7, 'Edward Davis', 'Printer', 1, '2024-04-07', 299.99),
(8, 'Frank White', 'Tablet', 2, '2024-04-08', 799.98),
(9, 'Grace Taylor', 'Speaker', 3, '2024-04-09', 449.97),
(10, 'Henry Martin', 'Camera', 1, '2024-04-10', 599.99); 