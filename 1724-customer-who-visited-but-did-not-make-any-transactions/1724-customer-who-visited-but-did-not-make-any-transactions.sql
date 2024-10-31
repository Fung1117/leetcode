# Write your MySQL query statement below
-- customer_id, COUNT(visit_id) AS count_no_trans
SELECT customer_id, COUNT(*) AS count_no_trans
FROM Visits v LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE transaction_id is NULL
GROUP BY customer_id;