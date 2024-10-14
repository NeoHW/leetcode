-- Write your PostgreSQL query statement below
SELECT current_day.id
FROM Weather as current_day
WHERE EXISTS (
    SELECT 1
    FROM Weather AS yesterday
    WHERE current_day.recordDate = yesterday.recordDate + 1
    AND current_day.temperature > yesterday.temperature
)
;