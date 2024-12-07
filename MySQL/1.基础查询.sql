# 基础查询

/* 
语法：
select 查询列表
from 表名;

特点:

1、查询列表可以是：表中的字段、常量值、表达式、函数
2、查询结果是一个虚拟的表格
*/
 
use myemployees;
 
# 1.查询表中的单个字段
select last_name from employees;

# 2.查询表中的多个字段
select last_name, salary, email from employees;

# 3.查询表中的所有字段  通过双击可以从navigator中加入字段
# ctrl+b 格式化
SELECT 
    employee_id, first_name, last_name, email, phone_number
FROM
    employees;

# ``着重号与关键字区分
select * from `employees`;

# 4.查询常量值
select 100;
select 'john';

# 5.查询表达式
select 100%98;

# 6.查询函数
select version();

# 7.别名
# 方式1
select last_name as 姓, first_name as 名 from employees;
# 方式2
select last_name 姓, first_name 名 from employees;
# 避免重名
select salary as 'out put' from employees;

# 8.去重
select department_id from employees; 
select distinct department_id from employees; 

# 9.+号的作用
/*
	select 100+90  加法运算
    select '123'+90 只要其中一方为字符型，试图将字符型数值转换为数值型
					如果转换成功，则继续做加法运算
	select 'john'+90 如果转换失败，将字符型数值转换为0
    select null+10 只要其中一方为null，则结果肯定为null
*/
# 查询员工名和姓连接成一个字段，并显示为 姓名
select last_name+first_name as 姓名 from employees;

select concat(last_name,' ',first_name) from employees;

# ifnull 如果是null值则输出指定值
select ifnull(commission_pct, 0), commission_pct from employees;
# isnull 如果是null值则输出1
select isnull(commission_pct), commission_pct from employees;
