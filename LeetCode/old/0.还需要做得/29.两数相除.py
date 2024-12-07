'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

示例 1:
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

示例 2:
输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2

'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0: return 0
        if divisor == 1: return dividend
        if divisor == -1:
            if dividend > -2**31:
                return -dividend
            else:
                return 2**31 - 1
        
        def div(divisor, layer):
            if divisor > dividend:
                return dividend, 0
            remain, ans = div(divisor + divisor, layer + layer)
            if remain >= divisor:
                return remain - divisor, ans + layer
            else:
                return remain, ans
        
        flag = 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            flag = 1
        dividend = abs(dividend)
        a, ans = div(abs(divisor), 1)
        ans = - ans if flag else ans
        return ans
        