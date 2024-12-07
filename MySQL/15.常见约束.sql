-- 约束
/*
    一种限制，用于限制表中的数据，为了保证表中的数据的准确和可靠性

    分类：六大约束
        NOT NULL：非空，用于保证该字段的值不能为空，例如姓名、学号、等
        DEFAULT：默认、用于保证该字段有默认值，例如性别
        PRIMARY KEY：主键，用于保证该字段的值具有唯一性，并且非空，比如学号、员工编号
        UNIQUE：唯一，用于保证该字段的值具有唯一性，可以为空 比如座位号
        CHECK：检查约束 mysql8.0.16才支持
        FOREIGN KEY：外键，用于限制两个表的关系，保证该字段的值必须来自于主表的关联列的值
    添加约束
        创建表时
        修改表时
    约束添加分类
        列级约束：六大约束语法上都支持，但外键约束没有效果
        表级约束：除了非空和默认，其他约束都支持

    主键和唯一对比：
        主键      保证唯一性    不允许为空    至多有一个null        允许组合，多个列构成主键，都重复时才重复  primary key（列1， 列2）
        唯一      保证唯一性    允许为空      可以有多个null        允许组合，多个列构成主键，都重复时才重复

    外键：
        1、要求在从表设置外键关系
        2、从表的外键列的类型和主表的关联列的类型要求一致或兼容，名称无要求
        3、主表的关联列必须是一个key（一般是主键或唯一）
        4、插入数据时，先插入主表，在插入从表
           删除数据时，先删除从表，再删除主表

        
*/

-- 一、创建表时添加约束
-- 1、添加列级约束
/*
    直接在字段名和类型后面追加约束类型即可
    只支持 默认、非空、主键、唯一
*/
CREATE DATABASE students;

USE students;

CREATE TABLE stuinfo(
    id INT PRIMARY KEY, -- 主键
    stuName VARCHAR(20) NOT NULL, --非空
    gender CHAR(1) CHECK(gender  = 'n' or gender = 'g'), -- 检查
    seat INT UNIQUE, -- 唯一
    age INT DEFAULT 18 -- 默认
);

CREATE TABLE major(
    id INT PRIMARY KEY,
    majorName VARCHAR(20)
);

DESC stuinfo;

-- 查看索引，包括主键、外键、唯一
SHOW INDEX FROM stuinfo;

INSERT INTO stuinfo
SET id = 10, stuName = 'he', gender = 'y';


-- 2、添加表级约束
/*
    语法：在各个字段的最下面
        【constraint 约束名】 约束类型（字段名）

*/
DROP TABLE IF EXISTS stuinfo;
DROP TABLE IF EXISTS major;
CREATE TABLE stuinfo(
    id INT ,
    stuName VARCHAR(20),
    gender CHAR(1),
    seat INT,
    age INT,
    majorID INT,

    CONSTRAINT pk PRIMARY KEY(id), -- 主键
    CONSTRAINT uq UNIQUE(seat), -- 唯一键
    CONSTRAINT ck CHECK(gender = 'nan' or gender = 'nv'), -- 检查
    CONSTRAINT fk_stuinfo_major FOREIGN KEY(majorID) REFERENCES major(id) -- 外键
);

SHOW INDEX FROM stuinfo;

-- 通用写法
DROP TABLE IF EXISTS stuinfo;
CREATE TABLE IF NOT EXISTS stuinfo(
    id INT PRIMARY KEY, -- 主键
    stuName VARCHAR(20) NOT NULL, --非空
    gender CHAR(1), -- 检查
    seat INT UNIQUE, -- 唯一
    age INT DEFAULT 18 -- 默认
    majorid INT,
    CONSTRAINT fk_stuinfo_major FOREIGN KEY(majorid) REFERENCES major(id)

);


-- 二、修改表时添加约束
/*
    1、添加列级约束
    alter table 表名 modify column 字段名 字段类型 新约束；

    2、添加表级约束
    alter table 表名 add 【constraint 约束名】 约束类型（字段名） 【外键的引用】
*/
DROP TABLE IF EXISTS stuinfo;
DROP TABLE IF EXISTS major;
CREATE TABLE stuinfo(
    id INT ,
    stuName VARCHAR(20),
    gender CHAR(1),
    seat INT,
    age INT,
    majorID INT
);

ALTER TABLE stuinfo MODIFY COLUMN stuname VARCHAR(20) NOT NULL;
ALTER TABLE stuinfo MODIFY COLUMN age INT DEFAULT 18;
ALTER TABLE stuinfo MODIFY COLUMN id INT PRIMARY KEY; -- 列级约束
ALTER TABLE stuinfo ADD PRIMARY KEY(id);  -- 表级约束
ALTER TABLE stuinfo ADD CONSTRAINT fk_stuinfo_major FOREIGN KEY(majorid) REFERENCES major(id);


-- 三、修改表时删除约束
-- 1、删除非空约束

-- 删除非空约束
ALTER TABLE stuinfo MODIFY COLUMN stuname VARCHAR(20) NULL;

-- 删除默认约束
ALTER TABLE stuinfo MODIFY COLUMN age INT;

-- 删除主键
ALTER TABLE stuinfo DROP PRIMARY KEY;

-- 删除唯一
ALTER TABLE stuinfo DROP INDEX seat;

-- 删除外键
ALTER TABLE stuinfo DROP FOREIGN KEY fk_stuinfo_major;

SHOW INDEX FROM stuinfo;