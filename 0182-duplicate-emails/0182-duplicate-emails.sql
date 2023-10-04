# Write your MySQL query statement below
SELECT distinct A.email as Email
FROM Person A, Person B
Where A.email = B.email and 
A.id <> B.id