# Write your MySQL query statement below
WITH max_salary AS (
SELECT
  MAX(Salary) AS max_salary,
  DepartmentId
FROM Employee
GROUP BY DepartmentId
),

max_salary_name AS (
SELECT
e.Name,
ms.max_salary AS Salary,
ms.DepartmentId
FROM max_salary ms
LEFT JOIN Employee e
ON e.DepartmentId=ms.DepartmentId AND e.Salary=ms.max_salary
)

SELECT
d.Name AS Department,
msn.Name AS Employee,
msn.Salary
FROM max_salary_name msn
LEFT JOIN Department d
ON msn.DepartmentId=d.Id