'''
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

示例 2：
输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"

示例 3：
输入：s = ""
输出：0
'''
class Solution:

    #动态规划
    def longestValidParentheses(self, s):
        if not s: return 0
        n = len(s)
        dp = [0] * n
        for i in range(n):
            if s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - dp[i - 1] - 2] + dp[i - 1] + 2
        return max(dp)
    '''
    动态规划

    状态空间        以元素i结尾的最长有效括号子串
    状态转移公式     dp[i] = dp[i - dp[i - 1] - 2] + dp[i - 1] + 2
    边界条件

    分情况判断 
    i == '('  一定不符合条件  dp = 0
    i == ')'  
        i - 1 == '('  在i-1前一个的基础上加2即可  dp[i]=dp[i−2]+2
        i - 1 == ')'  
            先确定前一个的最长子串  dp[i−1]  
            把i向左移 前一个的最长子串 的长度  i-dp[i - 1]-1  
                s[i-dp[i-1]-1] == '('
                说明这之间的都是有效子串  dp[i−1]+2
                最后再加上前面的最长子串  dp[i-dp[i-1]-2] + dp[i−1]+2

        可以发现i - 1 == '('情况下是i - 1 == ')'的一个特例
        可以用同一个状态转移公式求
        0 1 2 3 4 5 6 7 8
        ( ) ( ) ( ( ) ) )
        ↑
        0

        0 1 2 3 4 5 6 7 8
        ( ) ( ) ( ( ) ) )
        ↑
        0 2   

        0 1 2 3 4 5 6 7 8
        ( ) ( ) ( ( ) ) )
            ↑
        0 2 0  

        0 1 2 3 4 5 6 7 8
        ( ) ( ) ( ( ) ) )
            ↑
        0 2 0 4
            2+2   

        0 1 2 3 4 5 6 7 8
        ( ) ( ) ( ( ) ) )
                ↑
        0 2 0 4 0 0

        0 1 2 3 4 5 6 7 8
        ( ) ( ) ( ( ) ) )
                    ↑
        0 2 0 4 0 0 2

        0 1 2 3 4 5 6 7 8
        ( ) ( ) ( ( ) ) )
                    ↑
        0 2 0 4 0 0 2 8
                    4 + 2 + 2
    '''
    
s = "(()"
S = Solution()   
re = S.longestValidParentheses(s)
print(re)