# Write your MySQL query statement below
SELECT E.NAME AS NAME, B.BONUS AS BONUS
FROM Employee AS E
LEFT JOIN Bonus AS B
ON E.empId = B.empId
WHERE B.Bonus < 1000 or B.Bonus IS NULL