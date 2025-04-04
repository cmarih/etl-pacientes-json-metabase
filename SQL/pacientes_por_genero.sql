SELECT gender, 
    COUNT(*) AS total_pacientes
FROM patients
WHERE gender IN ('male', 'female')  
GROUP BY gender;