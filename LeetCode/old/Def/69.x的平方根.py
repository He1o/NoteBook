'''
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
'''

class Solution:
    def mySqrt(self, x):
        left, right, ans = 0, x, -1
        while left <= right:
            mid = (left + right) // 2  # 不用整除且mid前进小数即可得到非整数解
            if  mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right


# 牛顿迭代
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)   # 像是面积为C  长x0 宽C/x0  为了使长与宽相等 xi = (x0 + C / x0) / 2
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi
        
        return int(x0)

'''
如果使用 >= 或者 <   
left返回第一个大于等于目标值的数,如果存在目标数,则返回的就是该值,如果均小于
rihgt返回第一个小于该目标值的数,如果列表中均大于,指向-1

如果使用 > 或者 <=   
left返回第一个大于目标值的数,
rihgt返回第一个小于等于该目标值的数,如果存在目标数,则返回的就是该值
'''


s = 9
S = Solution()   
re = S.mySqrt(s)
print(re)    
                
            