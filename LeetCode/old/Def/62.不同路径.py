'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

示例 1：
输入：m = 3, n = 7
输出：28

示例 2：
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下

示例 3：
输入：m = 7, n = 3
输出：28

示例 4：
输入：m = 3, n = 3
输出：6
'''
from functools import lru_cache

class Solution:
    def uniquePaths(self, m, n):
        def backTrack(i, j):
            if i == m and j == n:
                return 1
            
            down = right = 0
            if i <= m and j <= n:
                down = backTrack(i + 1, j)
                right = backTrack(i, j + 1)
            
            return down + right
        return backTrack(1, 1)

    # 改进
    # 当到达边界时，实际上只有一条路可以到达终点了了因此返回1
    # 在本方法中是不会出现判断最后终点的情况的
    # 用内置函数缓存
    def uniquePaths(self, m, n):
        @lru_cache(None)
        def backTrack(i, j):
            if i == m or j == n:
                return 1
            return backTrack(i + 1, j) + backTrack(i, j + 1)
        return backTrack(1, 1)


    # 计算超时，因此需要缓存
    def uniquePaths(self, m, n):
        cache = {}
        def backTrack(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i == m or j == n:
                return 1
            cache[(i, j)] = backTrack(i + 1, j) + backTrack(i, j + 1)
            return cache[(i, j)]
        return backTrack(1, 1)

    # 动态规划
    def uniquePaths(self, m, n):
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

    # 动态规划 + 滚动数组
    def uniquePaths(self, m, n):
        dp = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]

        return dp[n - 1]

S = Solution()   
re = S.uniquePaths(3,7)
print(re)    