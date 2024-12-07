# 常见函数
/*
	概念：将一组逻辑语句封装在函数中，对外暴露方法名
    优点：1隐藏了实现细节 2提高代码的重用性
    调用：select 函数名（实参列表） from表alter
    分类：1单行函数
			 字符函数 
				length
                concat
                upper
                lower
                substr
                instr
                trim
                lpad
                rpad
                replace
			 数学函数
				round
                ceil
                floor
                truncate
                mod
                
		  2分组函数
*/
use myemployees;
# 一、字符函数
# 1.length 获取参数值的字节个数
select length('john');

# 2.concat 拼接字符串
select concat(last_name, '_', first_name) 姓名 from employees;

# 3.upper lower
select upper('john');
select lower('joHn');

# 4.substr substring
# 索引从1开始，截取从指定索引处后面所有字符
select substr('一二三四伍六七', 2) out_put;
# 索引从1开始，截取从指定索引处后面指定字符长度
select substr('一二三四伍六七', 2, 3) out_put;  #截取指定索引处指定字符长度的字符串，substr('一二三四伍六七', i, n)

# 5.instr
# 返回子串第一次出现的索引，如果找不到返回0
select instr('弱小和无知不是生存的障碍，傲慢才是', '傲慢') as out_put;

# 6.trim
# 剔除首尾指定元素
select trim('a' from 'aaaaabbbabbabbbbaaa') as out_put;

# 7.lpad 用指定字符实现左填充指定长度
select lpad('a', 12, 't');

# 8.rpad 用指定字符实现右填充指定长度
select rpad('a', 12, 't');

# 9.replace 替换
select  replace('aaaaaaaaddaaa', 'd', 't') as out_put;


# 二、数学函数
# round 四舍五入
select round(-1.55);
select round(1.567, 2);  #保留两位小数取整

# ceil 向上取整
select ceil(1.01); #2
select ceil(-1.01);  #-1

# floor 向下取整，返回<=该参数的最大整数
select floor(-2.2);

# truncate 截断
select truncate(1.69, 1);  #保留小数点后一位， 1.6

# mod 取余
select mod(-10, -3);


# 三、日期函数
# now 返回当前系统日期和时间
select now();

# curdate 返回日期，无时间
select curdate();

# curtime 返回时间
select curtime();

# 可以获取指定的部分， 年月日
select year('1998-02-22') 年;  # 输出年
select month('1998-02-22') 日;

# str_to_date 将字符通过指定的格式转换成日期
select str_to_date('4-3 1993',  '%c-%d %Y');

# date_format 将日期转换成字符
select date_format('2018/06/06', '%Y年%m月%d日');

# datediff 返回两个日期的相差天数
select datediff('2021-7-11', '1994-11-19');

# 四、其他函数
select database();  #当前数据库
select user(); #当前用户
select version(); #当前版本
select password('heao'); #加密

# 五、流程控制函数
-- if函数  if else效果alter
select if(10 < 5, '大', '小');
select last_name, commission_pct, if (commission_pct is null, '没奖金', '有奖金')
from employees;


# case函数
select salary 原始工资, department_id,
case department_id
when 30 then salary*2
when 30 then salary*3
else salary
end as 新工资
from employees;

# case elif用法
select salary,
case
when salary > 20000 then 'A'
when salary > 15000 then 'B'
when salary > 10000 then 'C'
else 'D'
end as 工资级别
from employees;