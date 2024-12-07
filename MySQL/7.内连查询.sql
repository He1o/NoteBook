# 连接查询
/*
	含义：又称为多表查询，当查询的字段来自于多个表时，就会用到连接查询
    语法：select  name_a, name_b from a, b
				笛卡尔乘积， 表a有m行，表b有n行，结果m*n行  
	分类：
			sql92标准
            sql99标准， mysql中支持内连接、外连接（不支持全外连接）、交叉连接
            
            功能分类：
            内连接：
				等值连接
                非等值连接
                自连接
			外连接：
				左外连接
                右外连接
                全外连接
			交叉连接
*/

use myemployees;

# sql92
# 一、内连接
#1、 等值连接
/*
    1.多表等值连接的结果为多表的交集部分，生成笛卡尔积取符合条件的，10x10x10 则有1000个结果筛选
    2.n表连接，至少需要n-1个连接条件
    3.多表的顺序没有要求
    4.一般需要为表起别名
    5.可以搭配查询子句使用，比如排序、分组、筛选
*/

# 案例1：查询员工名和对应的部门名
select last_name, department_name
from employees, departments
where employees.department_id = departments.department_id;

# 案例2:查询员工名、工种号、工种名
SELECT last_name, employees.`job_id`, job_title
FROM employees, jobs
WHERE employees.`job_id` = jobs.`job_id`;

# 起别名
/*
    提高语句简洁度
    区分多个重名的字段
    注意：如果为表起了别名，则查询的字段不能使用原来的表名去限定
*/
SELECT last_name, e.`job_id`, job_title
FROM employees as e, jobs as j
WHERE e.`job_id` = jobs.`job_id`;

# 加筛选
# 案例3:查询有奖金的员工名、部门名
SELECT last_name, department_name
FROM employees e, departments d
WHERE e.`department_id` = d.`department_id`
AND e.`commission_pct` IS NOT NULL; 

# 案例4:查询城市名中第二个字符为o的部门名和城市名
SELECT department_name, city
FROM departments d, locations l
WHERE d.`location_id` = l.`location_id`
AND city = '_o%';

# 加分组
# 案例5:查询每个城市的部门个数
SELECT count(*), city
FROM departments d, locations l
WHERE d.`location_id` = l.`location_id`
GROUP BY city;

# 案例6:查询有奖金的每个部门的部门名和部门的领导编号和该部门的最低工资
# SELECT后面的字段必须出现在group by后面，或者被聚合函数包裹
SELECT department_name, e.`department_id`, min(salary)
FROM departments d, employees e
WHERE  d.`department_id` = e.`department_id`
AND commission_pct IS NOT NULL
GROUP BY department_name, e.`department_id`;

# 加排序
# 案例7:查询每个工种的工种名和员工的个数，并且按员工个数降序
SELECT count(*), job_title 
FROM employees e, jobs j
WHERE e.`job_id` = j.`job_id`
GROUP BY e.`job_id`
ORDER BY count(*)
e.job_id;

# 多表连接
# 案例8:查询员工名、部门名和所在的城市
SELECT last_name, department_name, city
FROM employees e, departments d, locations l
WHERE e.department_id = d.department_id
AND d.location_id = l.location_id
AND city LIKE 's%';

#2、 非等值连接
# 案例1:查询员工的工资和工资级别
-- CREATE TABLE job_grades
-- (grade_level VARCHAR(3),
--  lowest_sal  int,
--  highest_sal int);

-- INSERT INTO job_grades
-- VALUES ('A', 1000, 2999);

-- INSERT INTO job_grades
-- VALUES ('B', 3000, 5999);

-- INSERT INTO job_grades
-- VALUES('C', 6000, 9999);

-- INSERT INTO job_grades
-- VALUES('D', 10000, 14999);

-- INSERT INTO job_grades
-- VALUES('E', 15000, 24999);

-- INSERT INTO job_grades
-- VALUES('F', 25000, 40000);

SELECT salary, grade_level
FROM employees e, job_grades g
WHERE salary BETWEEN g.`lowest_sal` AND g.`highest_sal`
AND g.`grade_level` = 'A';

#3、 自连接
# 案例1:查询员工名和上级的名称
SELECT e.employee_id as ei1, e.last_name as ln1, m.employee_id as ei2, m.last_name as ln2
FROM employees e, employees m
WHERE e.`manager_id` = m.`employee_id`; 