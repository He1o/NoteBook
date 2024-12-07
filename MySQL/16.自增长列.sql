-- 标识列
/*
    又称自增长列
    可以不用手动插入值，系统提供默认的序列值
    AUTO_INCREMENT

    特点：
    1、标识列不必和主键搭配，但要求是一个key
    2、一个表中只能有一个标识列
    3、标识列的类型只能是数值型
    4、标识列可以通过SET auto_increment_increment = 3设置步长
    5、可以通过手动插入值设置起始值
*/

-- 一、创建表时设置标识列
DROP TABLE IF EXISTS tab_identity;
CREATE TABLE tab_identity(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20)
);

INSERT INTO tab_identity VALUES(5, 'john'); -- 可以通过插入值改变起始值
INSERT INTO tab_identity(name) VALUES('john');

SELECT * FROM tab_identity;

SHOW VARIABLES LIKE '%auto_increment%';

SET auto_increment_increment = 3;

-- 二、修改表时设置标识列
ALTER TABLE tab_identity MODIFY COLUMN id INT PRIMARY KEY AUTO_INCREMENT;

-- 三、修改表时删除标识列
ALTER TABLE tab_identity MODIFY COLUMN id INT;

SHOW INDEX FROM tab_identity;