# Write your MySQL query statement below
Select p.firstName, p.lastName, a.city, a.state
From Person as p LEFT JOIN Address as a
ON p.personId= a.personId