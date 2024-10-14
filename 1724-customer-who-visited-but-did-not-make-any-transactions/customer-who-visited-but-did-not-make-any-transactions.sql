-- Write your PostgreSQL query statement below
SELECT v.customer_id , COUNT(*) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL -- we cannot use WHERE t.visit_id = NULL, also why is using t.amount wrong?
GROUP BY v.customer_id
;