# 分组函数
/*
	用作统计使用，又称聚合函数和统计函数或组函数
    分类：
		sum 求和
        avg 平均值
        max 最大值
        min 最小值
        count 个数
	特点：
		1、sum、avg一般用于处理数值型
		   max、min、count可以处理任何类型
		2、统计计算都是忽略null值  null与任何值计算结果都为null
        3、可以和distinct搭配使用
        4、count函数的单独介绍
*/

# 1、简单使用
select sum(salary) from employees;
select avg(salary) from employees;
select min(salary) from employees;
select max(salary) from employees;
select count(salary) from employees;

select sum(salary) 和,  avg(salary) 'avg', max(salary), min(salary), count(salary) from employees;


# 2、和distinct搭配使用
select sum(distinct salary), sum(salary) from employees;
select count(distinct salary), count(salary) from employees;

-- 3、count函数的具体使用
select count(salary) from employees;
select count(*) from employees;  -- 查询任何列中不为null的数量，只要一行中有一个不为null就统计下来
select count(1) from employees;  -- 在列表中加上一列都为1，统计1的个数
-- 效率 count(*)>count(1)>count(字段)   一般用count(*)进行行数统计