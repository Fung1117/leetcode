# Write your MySQL query statement below
SELECT id, 
CASE WHEN T1.p_id is NULL THEN "Root"
     WHEN  0 >= (SELECT COUNT(*) FROM TREE T2 WHERE T1.id = T2.p_id ) THEN "Leaf"
     ELSE "Inner"
END AS type
FROM TREE T1