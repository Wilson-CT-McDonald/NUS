# Q2
-- a) Insert a new customer record
INSERT INTO Customers (FirstName, LastName, Email, Mobile, Address)
VALUES ('Wilson', 'Zhao', 'wilsonwilson@gmail.com', '123456789', '123 Main St, Singapore');

-- b) Update a customer's email address
UPDATE Customers
SET Email = 'wilsonNewEmail@gmail.com'
WHERE CustomerID = 1;

-- c) Delete a specific order record (Need to create 1 first)
INSERT INTO orders (CustomerID, OrderDate,TotalAmount)
VALUES (1, '2024-03-01',100),(1, '2024-03-02',200),(1, '2024-03-03',300);

DELETE FROM Orders
WHERE OrderID = 1;