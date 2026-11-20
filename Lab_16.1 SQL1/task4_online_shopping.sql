CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price REAL NOT NULL
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE OrderDetails (
    detail_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE INDEX idx_orders_user_date ON Orders(user_id, order_date);

INSERT INTO Users VALUES (1, 'Ansika', 'ansika@shop.com'), (2, 'Vikram', 'vikram@shop.com');
INSERT INTO Products VALUES (1, 'Wireless Mouse', 799.0), (2, 'Mechanical Keyboard', 2499.0);
INSERT INTO Orders VALUES (101, 1, '2026-11-05'), (102, 2, '2026-11-12');
INSERT INTO OrderDetails VALUES (1, 101, 1, 2, 799.0), (2, 101, 2, 1, 2499.0), (3, 102, 1, 1, 799.0);

-- 1. All orders by user_id = 1
SELECT o.order_id, o.order_date, p.product_name, od.quantity, (od.quantity * od.unit_price) AS line_total
FROM Orders o
JOIN OrderDetails od ON o.order_id = od.order_id
JOIN Products p ON od.product_id = p.product_id
WHERE o.user_id = 1;

-- 2. Most purchased product
SELECT p.product_name, SUM(od.quantity) AS total_units
FROM OrderDetails od
JOIN Products p ON od.product_id = p.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_units DESC
LIMIT 1;

-- 3. Total revenue in November 2026
SELECT ROUND(SUM(od.quantity * od.unit_price), 2) AS nov_2026_revenue
FROM Orders o
JOIN OrderDetails od ON o.order_id = od.order_id
WHERE o.order_date LIKE '2026-11-%';
