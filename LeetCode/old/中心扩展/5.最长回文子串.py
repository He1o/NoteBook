'''
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

示例 3：
输入：s = "a"
输出："a"

示例 4：
输入：s = "ac"
输出："a"

'''

class Solution(object):
    # 第一次
    '''
    时间复杂度 O(n^2)  长度1和2的回文中心分别有n和n-1个，每个回文中心最多会向外扩展n次
    空间复杂度 O(1)
    '''
    def longestPalindrome1(self, s):
        n = len(s)
        def judge(i,j):
            while True:
                if i >= 0 and j < n and s[i] == s[j]:
                    i = i - 1
                    j = j + 1
                else:
                    return i + 1, j - 1
        start, end = 0, 0
        for center in range(len(s) - 1):
            left1, right1 = judge(center, center)
            left2, right2 = judge(center, center + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start : end + 1]
        
    # 第二次
    def longestPalindrome1(self, s):
        n = len(s)
        def Judge(i, j):
            result = []
            while i >= 0 and j < n and s[i] == s[j]:
                result = [i, j]
                i -= 1
                j += 1
            return result
        cnt = -1
        for i in range(n):
            result1 = Judge(i, i)
            result2 = Judge(i, i + 1)
            if result1 and result1[1] - result1[0] > cnt:
                ans = result1
                cnt = result1[1] - result1[0]
            if result2 and result2[1] - result2[0] > cnt:
                ans = result2
                cnt = result2[1] - result2[0]  
        return s[ans[0]:ans[1]+1]
         

'''
中心扩展
从中心开始判断当前两个指针指向的字母是否相等，随后左后退一步右前进一步判断是否相等
初始可以指向同一个，即为自己与自己相等长度为1
ababad
  ↑
ababad
 ↑ ↑
ababad
↑   ↑
1. 通过一个通用的函数去简化程序,而不是用if判断来考虑每一种情况
2. 归纳if条件能否放在一起，用同样or或and连接。
'''


s = 'bb'
S = Solution()   
# with timer.timer('time'):
re = S.longestPalindrome(s)
print(re)

            
                


                




                