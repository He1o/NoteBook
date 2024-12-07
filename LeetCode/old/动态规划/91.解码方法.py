'''
一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：

'A' -> 1
'B' -> 2
...
'Z' -> 26
要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：

"AAJF" ，将消息分组为 (1 1 10 6)
"KJF" ，将消息分组为 (11 10 6)
注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。

给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。

题目数据保证答案肯定是一个 32 位 的整数。

示例 1：
输入：s = "12"
输出：2
解释：它可以解码为 "AB"（1 2）或者 "L"（12）。

示例 2：
输入：s = "226"
输出：3
解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

示例 3：
输入：s = "0"
输出：0
解释：没有字符映射到以 0 开头的数字。
含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。

示例 4：
输入：s = "06"
输出：0
解释："06" 不能映射到 "F" ，因为字符串含有前导 0（"6" 和 "06" 在映射中并不等价）。

'''

class Solution:
    # 递归超时，应该可以优化
    def numDecodings(self, s):
        n = len(s)
        result = [0]
        def backTrack(pos):
            if pos == n:
                result[0] += 1
                return

            if pos <= n - 1 and int(s[pos]) > 0:
                backTrack(pos + 1)
            if pos <= n - 2 and 10 <= int(s[pos:pos+2]) <= 26:
                backTrack(pos + 2)

            return 
        backTrack(0)
        return result[0]

    # 动态规划 easy
    def numDecodings(self, s):
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for i in range(n):
            num1 = 0
            num2 = 0
            if s[i] != '0':
                num1 = dp[i]
            if i > 0 and 10 <= int(s[i - 1 : i + 1]) <= 26:
                num2 = dp[i - 1]
            dp[i + 1] = num1 + num2

        return dp[n]


s = "0"
S = Solution()   
re = S.numDecodings(s)
print(re)    

                