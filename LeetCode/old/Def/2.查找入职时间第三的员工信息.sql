use employees;

SELECT 
    *
FROM
    employees
WHERE
    hire_date = (
		SELECT 
			hire_date
        FROM
            employees
        ORDER BY hire_date DESC
        LIMIT 3
        OFFSET 2);