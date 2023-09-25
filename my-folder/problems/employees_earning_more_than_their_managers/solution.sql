# Write your MySQL query statement below

SELECT e.name as Employee
FROM Employee E, Employee M
where E.managerId=M.id
and E.salary>M.salary
