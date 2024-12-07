'''
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

示例 1：
输入：x = 121
输出：true

示例 2：
输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3：
输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。

示例 4：
输入：x = -101
输出：false
'''
# 方法一  字符串
a = 123
str_a = list(str(a))
i = 0
j = len(str_a) - 1
while i <= j:
    if str_a[i] != str_a[j]:
        break
    i += 1
    j -= 1


# 方法二 数学计算
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        num = x
        rev = 0
        while num > rev:
            a = num % 10
            rev = rev * 10 + a
            num = num // 10
        return (num == rev) or (num == rev // 10)

'''  
1. 反转数字，判断到达终点，当后部分比前面大或等于时  12 < 123  即为过半
12321
   ↑
2. 尾数为0时需要特殊考虑
'''

