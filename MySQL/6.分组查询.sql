# 分组查询
/*
	语法：
		select 分组函数，列（要求出现在group by的后面）
        from 表
        【where 筛选条件】
        group by 分组的列表
        【order by 子句】
	注意：
		查询列表必须特殊，要求分组函数和group by后出现的字段
	总结：
		1、 分组查询中的筛选条件分为两类
							数据源					位置				   关键字
			分组前筛选      原始表                  group by子句前         where
            分组后筛选      分组后的结果            group by子句前         having
            
            分组函数做条件一定在having子句中
            能用分组前筛选的，优先考虑分组前
		2、分组函数不必出现在select中！！！！！！
*/
use myemployees;
# 案例1 查询每个工种的最高工资
select max(salary), job_id from employees group by job_id;

# 案例2 查询每个位置上的部门个数
select count(*), location_id from departments group by location_id;

# 案例3 查询邮箱中包含a字符的，每个部门的平均工资[添加where筛选条件]
select avg(salary), department_id
from employees
where email like '%a%'
group by department_id;

# 案例4 查询有奖金的每个领导手下员工的最高工资[添加where筛选条件]
select max(salary), manager_id
from employees
where commission_pct is not null
group by manager_id;

# 案例5 查询哪个部门的员工个数大于2[添加having筛选条件]   通过select后的结果筛选用having，where只能在group之前
select count(*), department_id
from employees
group by department_id
having count(*) > 2;

# 案例6 查询每个工种有奖金的员工的最高工资>12000的工种编号和最高工资[添加having筛选条件]
select max(salary), job_id
from employees
where commission_pct is not null
group by job_id
having max(salary) > 12000;

# 案例7 查询领导编号>102的每个领导手下的最低工资>5000的领导编号[添加筛选条件]
select min(salary), manager_id
from employees
where manager_id > 102
group by manager_id
having min(salary) > 5000;

# 案例：按员工姓名的长度分组，查询每一组的员工个数，筛选员工个数>5的有哪些[按表达式或函数分组]
select count(*) , length(last_name)
from empoyees
group by length(last_name)
having count(*) > 5;

# 案例：查询每个部门每个工种的员工平均工资[按多个字段分组]
select avg(salary), department_id, job_id
from employees
group by department_id, job_id;


# 查询每个部门每个工种员工的平均工资，并且按平均工资的高低排序[添加排序]
select avg(salary), department_id, job_id
from employees
group by department_id, job_id
order by avg(salary);

# 查询各个管理者手下员工的最低工资，其中最低工资不能低于6000，没有管理者的员工不计算在内
select min(salary), manager_id
from employees
where manager_id is not null
group by manager_id
having min(salary) >= 6000;

