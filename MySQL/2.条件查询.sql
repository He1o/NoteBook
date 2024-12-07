# 条件查询
/* 
	select 
		查询列表
	from
		表明
	where
		筛选条件
	一、按条件表达式筛选
		条件运算符 > < = != >= <=
	二、逻辑表达式筛选
		逻辑运算符 && || ！  and or not
	三、模糊查询
			like
            between and
            in
            is null
*/
#-------------------------------------------------------------------------
# 一、按条件表达式筛选
# 案例1：查询工资大于12000的员工信息
select * from employees where salary > 12000;
# 案例2：查询部门编号不等于90号的员工名和部门编号
select last_name,department_id from employees where department_id<>90;

#-------------------------------------------------------------------------
# 二、逻辑表达式筛选
# 案例1：查询工资在10000和20000之间的员工名、工资以及奖金
SELECT 
    last_name, salary, commission_pct
FROM
    employees
WHERE
    salary >= 10000 AND salary <= 20000;
# 案例2：查询部门编号不是在90到110之间、或者工资高于15000的员工信息
SELECT 
    *
FROM
    employees
WHERE
    department_id < 90
        OR department_id > 110
        OR salary > 15000;
        
SELECT 
    *
FROM
    employees
WHERE
    NOT (90 <= department_id and department_id <= 110)
        OR salary > 15000;
        
#-------------------------------------------------------------------------        
# 三、模糊查询
/*
like 
	1. 一般与通配符一块使用，可以用于判断字符型或数值型
		% 任意多个字符，包含0个字符
        _ 任意单个字符
        \ 转义字符 或通过escape定义转义字符
*/
# 案例1：查询员工中包含字符a的员工信息
select * from employees where last_name like '%a%';
select * from employees where last_name like '_a__a%';
select * from employees where last_name like '_a_$_a%' escape '$';

/*
between and
	1. 可以提高语句简洁度
    2. 包换两个临界值
    3. 临界值不可以调换顺序
*/
# 案例2：查询员工编号在100到120之间的员工信息
select * from employees where employee_id between 100 and 120;

/*
in
	1. 可以提高语句简洁度
    2. IN列表的值类型必须一致或兼容
    3. 不支持通配符
*/
# 案例3：查询员工的工种编号是 IT_PROG、AD_VP、AD_PRES中的一个员工名和工种编号
select last_name,job_id from employees where job_id = 'IT_PROG' or job_id = 'AD_VP' or job_id = 'AD_PRES';
select last_name,job_id from employees where job_id in ('IT_PROG','AD_VP','AD_PRES');

/*
is NULL
	1. =或者<>不能用于判断null值
    2. is null 或 is not null可以判断
    3. <=> 安全等于可以判断null也可以判断值, 可读性差
*/
select last_name,commission_pct from employees where commission_pct is null;
select last_name,commission_pct from employees where commission_pct <=> null;