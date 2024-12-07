'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);
示例 1：
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

示例 3：
输入：s = "A", numRows = 1
输出："A"

'''
s = 'sdfwerwer'
n = 1
ans = [[] for _ in range(n)]
i = 0
x = ''
flag = False
for item in s:
    ans[i].append(item)
    
    if i == n - 1 or i == 0:
        flag = not flag

    i = i + 1 if flag else i - 1
    x = ''.join(str(aa) for a in ans for aa in a)
print(x)


# 第二次
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        strlist = ['' for _ in range(numRows)]
        row = 0
        flag = False
        for letter in s:
            strlist[row] += letter
            if row == (numRows - 1) or row == 0: flag = not flag
            
            if flag : 
                row += 1
            else:
                row -= 1

        return ''.join(strlist)


'''
竟然能想出标准答案，看到评论里一堆说目瞪口呆的，想想自己也不算笨
1. 合并if  bool = not bool
2. if else条件判断语句同一行赋值
3. 列表中无需是列表，字符串就可以操作
'''