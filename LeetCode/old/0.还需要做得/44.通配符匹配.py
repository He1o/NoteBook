'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。
说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。

示例 3:
输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。

示例 4:
输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".

示例 5:
输入:
s = "acdcb"
p = "a*c?b"
输出: false
'''

class Solution:
    def isMatch(self, s, p):
        n = len(s)
        m = len(p)
        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0]= True

        for i in range(1, m + 1):
            if p[i - 1] == '*':
                f[0][i] = True
            else:
                break
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    f[i][j] = (f[i][j - 1] | f[i - 1][j])
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    f[i][j] = f[i - 1][j - 1]
        return f[n][m]


    # 第二次
    # 难点在于边界条件的确立
    # 对于这个状态转移方程，dp[0][j]与dp[i][0]均为边界条件，涉及到空字符串的情况
    # dp[0][0] True 均为空时匹配成功
    # dp[i][0] False 空字符串无法匹配字符串
    # dp[0][j] 分情况，当p的前j个字符均为星号时匹配成功
    def isMatch(self, s, p):
        '''
        时间复杂度 O(mn) 双循环，一个字符串遍历中遍历另个字符串
        空间复杂度 O(mn) 可以用滚动数组优化 两个长度为n+1的一维数组代替整个二维数组，降为O(n)
        '''
        n = len(s)
        m = len(p)
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        for j in range(m):
            if p[j] == '*':
                dp[0][j + 1] = True
            else:
                break

        for i in range(n):
            for j in range(m):
                if p[j] == s[i] or p[j] == '?':
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == '*':
                    dp[i + 1][j + 1] = dp[i][j + 1] | dp[i + 1][j]
        return dp[n][m]


    #贪心算法
    def isMatch(self, s: str, p: str) -> bool:
        def allStars(st: str, left: int, right: int) -> bool:
            return all(st[i] == '*' for i in range(left, right))
        
        def charMatch(u: str, v: str) -> bool:
            return u == v or v == '?'

        sRight, pRight = len(s), len(p)
        while sRight > 0 and pRight > 0 and p[pRight - 1] != '*':
            if charMatch(s[sRight - 1], p[pRight - 1]):
                sRight -= 1
                pRight -= 1
            else:
                return False
        
        if pRight == 0:
            return sRight == 0
        
        sIndex, pIndex = 0, 0
        sRecord, pRecord = -1, -1
        while sIndex < sRight and pIndex < pRight:
            if p[pIndex] == '*':
                pIndex += 1
                sRecord, pRecord = sIndex, pIndex
            elif charMatch(s[sIndex], p[pIndex]):
                sIndex += 1
                pIndex += 1
            elif sRecord != -1 and sRecord + 1 < sRight:
                sRecord += 1
                sIndex, pIndex = sRecord, pRecord
            else:
                return False

        return allStars(p, pIndex, pRight)



s = "adceb"
p = "*a*b"
S = Solution()   
re = S.isMatch(s, p)
print(re)