# 排序查询

/*
	语法：
		select 查询列表
        from 表
        where 筛选条件
        order by 排序列表 asc|desc
			如果不写、默认升序
	特点：
		order by 子句可以支持单个字段、多个字段、表达式、函数、别名
        order by 子句一般放在最后面
	
*/

use myemployees;

# 案例1：查询员工信息，要求工资从高到低排序
select * from employees order by salary desc;
select * from employees order by salary asc;

# 案例2：查询部门编号大于等于90的员工信息，按入职时间的先后进行排序
select * from employees where department_id >= 90 order by hiredate asc;

# 案例3：按年薪的高低显示员工的信息和年薪 [按表达式排序]
select *, salary*12*(1+ifnull(commission_pct,0)) 年薪
from employees
order by salary*12*(1+ifnull(commission_pct,0)) desc;

# 案例4：按年薪的高低显示员工的信息和年薪 [按别名排序]
select *, salary*12*(1+ifnull(commission_pct,0)) 年薪
from employees
order by 年薪 desc;

# 案例5：按姓名的长度显示员工的姓名和工资[按函数排序]
select length(last_name) 字节长度,last_name, salary
from employees
order by length(last_name) desc;

#案例6：查询员工信息，要求先按员工升序，再按员工编号排序[按多个字段排序]
select *
from employees
order by salary asc, employee_id desc;

