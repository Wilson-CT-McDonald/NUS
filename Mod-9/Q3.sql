# Q3
-- Insert some valid data first
INSERT INTO orders (CustomerID, OrderDate,TotalAmount)
VALUES (1, '2024-01-01',550);

SELECT OrderID, OrderDate, TotalAmount
FROM Orders
WHERE OrderDate BETWEEN '2024-01-01' AND '2024-01-31'
AND TotalAmount > 500;