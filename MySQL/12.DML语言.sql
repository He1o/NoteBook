-- DML语言
/*
    数据操作语言：
    插入：insert
    修改：update
    删除：delete
*/

-- 一、插入语句
/*
    语法：
        insert into 表名（列名，...）
        values(值1，....)
    要求：
        插入的值的类型要与列的类型一致或兼容
        不可以为null的列必须插入值
        可以为null的列可以输入null也可以省略不写
        列名写出来的话与values必须纬度一样
*/
-- 方式1
-- 类型保持一致
CREATE TABLE test
(grade_level VARCHAR(3),
 lowest_sal  int,
 highest_sal int);

INSERT INTO test
VALUES ('A', 1000, 2999);


-- 可以为null，可以省略，默认null
INSERT INTO test
VALUES ('B', 1000, NULL);

-- 列的顺序可以调换，  
INSERT INTO test(grade_level, highest_sal, lowest_sal)
VALUES ('C', 1, 3);

-- 可以省略列名，默认所有列，而且列的顺序和表中列顺序一致
SELECT * FROM test;


-- 方式2
/*
    语法：
        insert into 表名
        set 列名=值，列名=值
*/
INSERT INTO test
SET grade_level = 'E';


-- 比较
-- 方式1支持插入多行
INSERT INTO test(grade_level, highest_sal, lowest_sal)
VALUES ('C', 1, 3),
        ('C', 1, 3),
        ('C', 1, 3);

-- 方式1支持子查询
INSERT INTO test(grade_level, highest_sal, lowest_sal)
SELECT 'X',2,5;


-- 二、修改语句
/*
    1.修改单表中的记录
        语法：
            update 表名
            set 列=新值，列=新值，..
            where 筛选条件；
    2.修改多表的记录
        92语法：
            update 表1 别名， 表2 别名
            set 列=值
            where 连接条件
            and 筛选条件；

        99语法：
            update 表1 别名
            inner|left|right  join 表2 别名
            on 连接条件
            set 列=值,...
            where 筛选条件；
*/

UPDATE test
SET lowest_sal = 999
WHERE grade_level = 'X';

UPDATE test
SET lowest_sal = 20020,
    highest_sal = 26000
WHERE grade_level = 'C';

-- 三、删除语句
/*
    delete
    语法：
    单表删除
        delete from 表名 where 筛选条件
    多表删除

    truncate
    语法：
        truncate table 表名

    比较：
        1.delete可以加where条件， truncate不能加
        2.truncate删除效率高
        3.如果用delete删除后，在插入数据，自增长列的值从断点开始
          TRUNCATE删除后，插入数据，自增长列的值从头开始
        4.truncate删除没有发返回值
          delete有返回值，返回影响几行
        5.truncate是DDL语句，delete是DML语句，truncate删除不能回滚，delete删除可以回滚
        6.当你不再需要该表时， 用 drop；
          当你仍要保留该表，但要删除所有记录时， 用 truncate；
          当你要删除部分记录时（always with a WHERE clause), 用 delete.

*/
-- 方式1 delete
DELETE FROM test WHERE grade_level = 'C';

-- DELETE b
-- FROM beauty b
-- INNER JOIN boys bo ON b.'boyfriend_id' = bo.'id'
-- WHERE bo.'boyName' = 'Able';


-- 方式2 truncate
TRUNCATE TABLE test;

DESC jobs;