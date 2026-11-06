SELECT
    m.employee_id,
    m.name,
    COUNT(e.employee_id) AS reports_count,
    ROUND(AVG(e.age)) AS average_age
FROM Employees AS m
JOIN Employees AS e
    ON e.reports_to = m.employee_id
GROUP BY
    m.employee_id,
    m.name
ORDER BY
    m.employee_id;
