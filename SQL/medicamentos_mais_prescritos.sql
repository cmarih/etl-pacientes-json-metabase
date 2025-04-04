SELECT medication_name, COUNT(*) AS total_prescricoes
FROM medications
GROUP BY medication_name
ORDER BY total_prescricoes DESC
LIMIT 10;