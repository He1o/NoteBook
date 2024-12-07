'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

示例 1：
输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

示例 2：
输入：obstacleGrid = [[0,1],[0,0]]
输出：1
'''

class Solution:
    # 归纳的十分巧妙
    # 由于障碍物的存在每个点都需要判断
    # 初始dp可当做边界之上的路线均为0，但起点为1，表示起点是有一条路的
    # 左边界之外也是没有路的，想要用滚动数组的话，又不能多加一列（其实也可以，初始为1，i>0之后该值为0）
    # 只在j>0时进行动态转移，那么只有存在障碍物时第一列的值为0，其余为1
    # 那么只需要维护一个长度n的dp数组
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0 for _ in range(n)]
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] = dp[j] + dp[j - 1]
        
        return dp[n - 1]

s = [[0],[1]]
S = Solution()   
re = S.uniquePathsWithObstacles(s)
print(re)    