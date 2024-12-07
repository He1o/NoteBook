/*
    联合查询
    union：将多条查询语句的结果合并成一个结果

    语法：
        查询语句1
        union
        查询语句2
        UNION
        ...
    应用场景：
        要查询的结果来自于多个表，且多个表没有连接关系，即列名不一样
        但查询结果要求列数一样
    特点：
        1、要求多条查询语句的查询列数是一致的
        2、要求多条查询语句的查询的每一列的类型和顺序最好一致
        3、union关键字默认去重，加all可以保留重复项
*/

-- 案例1:查询部门编号》90或邮箱包含a的员工信息
SELECT * FROM employees WHERE email LIKE '%a%' or department_id > 90;

SELECT * FROM employees WHERE email LIKE '%a%'
UNION
SELECT * FROM employees WHERE department_id > 90;

-- 