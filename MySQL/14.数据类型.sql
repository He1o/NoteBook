-- 常见的数据类型
/*
    数值型：
        整型
            tinyint      1字节   8位   -128～127
            smallint     2字节  16位    万级别
            mediumint    3字节  24位    百万级别
            int|integer  4字节  32位    十亿级别
            bigint       8字节  64位
            特点：
                1.如果不设置无符号还是有符号，默认有符号，添加unsigned设置无符号
                2.如果插入数值超过整型的范围，会报out of range异常，并且插入临界值
                3.如果不设置长度，会有默认长度，长度代表显示的最大宽度
                    如果不够会用0在左边填充，但需要搭配zerofill使用
        小数：
            浮点数
                float(M,D)    4字节
                double(M,D)   8字节
            定点数
                DEC(M,D)      M+2
            特点：
                1.M 代表整数部位+小数部位
                  D 代表小数部位
                2.M和D都可以省略
                    decimal 默认M为10，D为0
                    float|double 则会根据插入的数值的精度来决定精度
                3.定点型的精确度较高，如果要求插入数值的精度较高如货币运算
        原则：
            所选择的类型越简单越好，能保存数值的类型越小越好
    字符型：
        较短的文本  
            char(M)      M最多字符数  可以省略默认1   0~255     固定长度                              空间耗费大    效率高
            varchar(M)   M最多字符数  不可以省略     0~65535   可变长度：根据输入字符串长度分配空间       空间耗费小    效率低
            ENUM 枚举类型
                要求插入的值必须属于列表中指定的值之一
                成员为1～255  需要1字节
                成员为255～65535  需要2字节
            SET 集合类型 
                可以保存0～64个成员
                和enum不同在于依次可以选取多个成员
        较长的文本  
            text、blob 
    日期型：
        data       4字节      1000-01-01  
        datatime   8字节      1000-01-01 00:00:00
        timestamp  4字节      19700101080001
        time       3字节      -838:59:59
        year       1字节      1901
*/

-- 整型
-- 案例1:设置有符号和无符号
DROP TABLE IF EXISTS tab_int;
CREATE TABLE tab_int(
    t1 INT(7) zerofill,
    t2 INT UNSIGNED
);
DESC tab_int;
INSERT INTO tab_int VALUES(10, 10);
SELECT * FROM tab_int;

-- 小数
DROP TABLE IF EXISTS tab_float;
CREATE TABLE tab_float(
    f1 FLOAT(5,2),
    f2 DOUBLE(5,2),
    f3 DECIMAL(5,2)
);
DESC tab_float;
INSERT INTO tab_float VALUES(123.45, 123.45, 123.45);
INSERT INTO tab_float VALUES(123.456, 123.456, 123.456);
INSERT INTO tab_float VALUES(123.4, 123.4, 123.4);

-- 字符串
CREATE TABLE tab_char(
    c1 ENUM('a', 'b', 'c')
);

INSERT INTO tab_char VALUES('a');
INSERT INTO tab_char VALUES('b');
INSERT INTO tab_char VALUES('d');

CREATE TABLE tab_set(
    s1 SET('a', 'b', 'c', 'd')
);

INSERT INTO tab_set VALUES('a,b,c');
INSERT INTO tab_set VALUES('a,e,c');
SELECT * FROM tab_set;


-- 日期
CREATE TABLE tab_date(
    t1 DATETIME,
    t2 TIMESTAMP
);

INSERT INTO tab_date VALUES(NOW(), NOW());
SELECT * FROM tab_date;

SHOW variables LIKE 'time_zone',