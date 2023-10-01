# Write your MySQL query statement below
SELECT name
FROM SalesPerson
WHERE name NOT IN (SELECT S.name
FROM SalesPerson S, Company C, Orders O
WHERE C.name = 'RED'
AND C.com_id = O.com_id
AND O.sales_id =  S.sales_id);