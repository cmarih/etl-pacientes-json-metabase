SELECT DATE_TRUNC('month', prescription_date) AS mes, COUNT(*) AS total_prescricoes
FROM medications
GROUP BY mes
ORDER BY mes;