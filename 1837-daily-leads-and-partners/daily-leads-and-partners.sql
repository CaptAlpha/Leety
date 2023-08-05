# Write your MySQL query statement below
SELECT DATE_ID, MAKE_NAME, COUNT(DISTINCT lead_id) AS unique_leads, COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name