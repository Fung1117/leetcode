# Write your MySQL query statement below]
SELECT name as Customers 
From Customers 
Where id not in (
  SELECT customerId
  FROM Orders
)