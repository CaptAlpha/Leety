# Write your MySQL query statement below
SELECT T2.name AS Employee
FROM Employee AS T1
JOIN Employee AS T2
ON T1.id = T2.managerId
WHERE T2.salary > T1.salary