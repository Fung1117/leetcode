# Write your MySQL query statement below
SELECT distinct A.num as ConsecutiveNums
FROM Logs A, Logs B, Logs C
WHERE A.id + 1 = B.id  and A.id + 2 = C.id
and A.num = B.num and A.num = C.num
