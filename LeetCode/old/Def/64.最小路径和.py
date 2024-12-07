'''
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。


示例 1：
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

示例 2：
输入：grid = [[1,2,3],[4,5,6]]
输出：12
'''
class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        dp = [float('inf') for _ in range(n)]
        dp[0] = 0

        for i in range(m):
            for j in range(n):
                if j > 0:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
                else:
                    dp[j] = dp[j] + grid[i][j]
        
        return dp[n - 1]


    # 在j开始前面对0进行操作不就行了吗
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        dp = [20001] * n
        dp[0] = 0

        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

        return dp[n - 1]


s = [[1,3,1],[1,5,1],[4,2,1]]
S = Solution()   
re = S.minPathSum(s)
print(re)    
