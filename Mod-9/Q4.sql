# Q4
-- Insert sample products
INSERT INTO Products (ProductName, Price, InventoryQuantity)
VALUES ('Laptop', 1200.00, 10),
       ('Smartphone', 800.00, 20),
       ('Tablet', 500.00, 15);

-- Insert sample orders in June 2024
INSERT INTO Orders (CustomerID, OrderDate, TotalAmount)
VALUES (1, '2024-06-05', 2000.00),
       (1, '2024-06-15', 1300.00);

-- Insert sample order details
INSERT INTO OrderDetails (OrderID, ProductID, Quantity)
VALUES (1, 1, 1),
       (2, 2, 2),
       (2, 3, 1);
       
SELECT P.ProductName, OD.Quantity AS QuantityOrdered, O.OrderDate
FROM OrderDetails OD
JOIN Orders O ON OD.OrderID = O.OrderID
JOIN Products P ON OD.ProductID = P.ProductID
WHERE O.OrderDate BETWEEN '2024-06-01' AND '2024-06-30';