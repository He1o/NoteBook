-- DDL
/*
    数据定义语言
    用于库和表的管理
    一、库的管理
        创建、修改、删除
    二、表的管理
        创建、修改、删除
    创建：create
    修改：alter
    删除：drop
*/

-- 一、库的管理
/* 
    1、库的创建
        create database 库名

    2、库的修改
        alter datebase 库名 字符集
    
    3、库的删除
        drop database 库名
*/

CREATE DATABASE IF NOT EXISTS books;

ALTER DATABASE books character set gbk;

DROP DATABASE IF EXISTS books;

use books;
-- 二、表的管理
/*
    1、表的创建
        create table 表名（
            列名  类型【（长度） 约束】，
            列名  类型【（长度） 约束】，
            ...
        ）
*/

-- 案例：创建表book
CREATE Table book(
    id INT,
    bName VARCHAR(20), -- 一个字母一个汉字都是一个字符
    price DOUBLE,
    author INT,
    publishDate DATETIME
);

-- 案例2:创建表author
CREATE Table author(
    id INT,
    au_name VARCHAR(20),
    nation VARCHAR(10)
);

/*
    2、表的修改
        修改列名
        修改列的类型或约束
        添加新列
        删除列
        修改表名
    alter table 表名
    add|drop|modify|change column 列名 【列类型 约束】
*/

-- 1.修改列名
ALTER Table book CHANGE COLUMN publishdate pubDate DATETIME;

-- 2.修改列的类型
ALTER Table book MODIFY COLUMN pubdate TIMESTAMP;

-- 3.添加新列
ALTER Table author ADD COLUMN annual DOUBLE;

-- 4.删除列
ALTER Table author DROP COLUMN annual;

-- 5.修改表名
ALTER Table author RENAME TO book_author;


/*
    3、表的删除

*/

DROP Table book_author;
SHOW TABLES;


-- 通用写法

DROP DATABASE IF EXISTS old_name;
CREATE DATABASE new_database;

DROP TABLE IF EXISTS old_name;
CREATE TABLE new;


/*
    4、表的复制
*/
INSERT INTO author VALUES
(1,'cunshangcunshu','japan'),
(2,'jinyong','china'),
(3,'moyan','china');

-- 1.仅复制表的结构
CREATE TABLE copydata LIKE author;

-- 2.复制表的结构和数据
CREATE TABLE copydata2 
SELECT * FROM author;

-- 3.仅复制表的部分结构,通过select复制列,通过where筛掉所有数据
CREATE TABLE copydata3 
SELECT id,au_name
FROM author
WHERE 0;