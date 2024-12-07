'''
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
'''

class Solution:
    def addBinary(self, a, b):

        add = 0
        i, j = len(a) - 1, len(b) - 1
        result = []
        while i >= 0 or j >= 0 or add:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0

            s = x + y + add
            result  = [str(s % 2)] + result
            add = s // 2

            i -= 1
            j -= 1

        return ''.join(result)

a = "1010"
b = "1011"
S = Solution()   
re = S.addBinary(a, b)
print(re)    


