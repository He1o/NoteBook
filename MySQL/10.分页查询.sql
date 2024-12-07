-- 分页查询
/*
    应用场景：当要显示的数据一页显示不全，需要分页提交sql请求
    语法：
        select 查询列表
        from 表
        【join type】 join 表2
        on 连接条件
        where 筛选条件
        group by 分组字段
        having 分组后筛选
        order by 排序的字段
        limit 【offset 要显示条目起始索引，从0开始】
              size 条目个数
    特点：
        limit语句放在查询语句的最后
        

*/

-- 案例1:查询前五条员工信息
SELECT *
FROM employees
LIMIT 5;

SELECT *
FROM employees
LIMIT 10,5;


-- ！！子查询题目！！
-- 1、查询工资最低的员工信息：last_name, salary
SELECT last_name, salary
FROM employees
WHERE salary = (
    SELECT MIN(salary)
    FROM employees
);

-- 2、查询平均工资最低的部门信息
SELECT *
FROM departments
WHERE department_id = (
    SELECT e.department_id
    FROM employees e
    GROUP BY department_id
    ORDER BY AVG(salary)
    LIMIT 1
); -- 分组函数不必出现在select后面也可以进行分组查询！！！！

-- 3、查询平均工资最低的部门信息和该部门的平均工资
SELECT *
FROM (
    SELECT e.department_id, AVG(salary) av_salary
    FROM employees e
    GROUP BY department_id
    ORDER BY av_salary
    LIMIT 1
) a
INNER JOIN departments d
ON d.department_id = a.department_id;

-- 4、查询平均工资最高的job信息
SELECT *
FROM jobs
WHERE job_id = (
    SELECT job_id
    FROM employees
    GROUP BY job_id
    ORDER BY AVG(salary) DESC
    LIMIT 1
);

-- 5、查询平均工资高于公司平均工资的部门有哪些？
-- SELECT AVG(salary)
-- FROM employees

-- SELECT AVG(salary)
-- FROM employees
-- GROUP BY department_id

SELECT AVG(salary)
FROM employees
GROUP BY department_id
HAVING AVG(salary) > (
    SELECT AVG(salary)
    FROM employees
);

-- 6、查询出公司中所有manager的信息
SELECT *
FROM employees
WHERE employee_id in (
    SELECT manager_id
    FROM departments
);

-- 7、各个部门中最高工资中最低的那个部门的最低工资是多少
SELECT department_id
FROM employees
GROUP BY department_id
ORDER BY MAX(salary);

SELECT salary
FROM employees
WHERE department_id = (
    SELECT department_id
    FROM employees
    GROUP BY department_id
    ORDER BY MAX(salary)
    LIMIT 1
)
ORDER BY salary
LIMIT 1;

-- 8、查询平均工资最高的部门的manager的详细信息，last_name, department_id, email, salary
