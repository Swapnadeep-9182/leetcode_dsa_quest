-- Write your PostgreSQL query statement below
SELECT eu.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUni eu
ON e.id = eu.id
