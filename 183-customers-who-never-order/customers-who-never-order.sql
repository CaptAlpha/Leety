# Write your MySQL query statement below
SELECT name AS CUSTOMERS
FROM Customers AS C
LEFT JOIN ORDERS AS O
ON C.ID = O.customerId
WHERE O.customerId IS NULL
