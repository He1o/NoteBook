'''
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]

示例 2：
输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

示例 3：
输入：matrix = [[1]]
输出：[[1]]

示例 4：
输入：matrix = [[1,2],[3,4]]
输出：[[3,1],[4,2]]
'''

class Solution:
    # 旋转
    def rotate1(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for x in range(n // 2):
            for y in range((n + 1) // 2):
                temp = matrix[x][y]
                matrix[x][y] = matrix[n - y -1][x]
                matrix[n - y -1][x] = matrix[n - x -1][n - y -1]
                matrix[n - x -1][n - y -1] = matrix[y][n - x -1]
                matrix[y][n - x -1] = temp
    
    def rotate(self, matrix):
        n = len(matrix)
        m = (n + 1) // 2
        for i in range(m):
            for j in range(m):
                temp = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = matrix[i][j]
                matrix[i][j] = temp


    # 折叠
    # def rotate(self, matrix):
    #     # TODO
    #     return



matrix = [[1,2,3],[4,5,6],[7,8,9]]
S = Solution()   
re = S.rotate(matrix)
print(matrix)