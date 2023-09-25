# Write your MySQL query statement below
Select email as Email
FROM Person
GROUP BY email 
having count(email)>1