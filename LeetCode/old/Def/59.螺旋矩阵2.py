'''
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

示例 1：
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

示例 2：
输入：n = 1
输出：[[1]]
'''

class Solution:
    def generateMatrix(self, n):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        up = 0
        down = n - 1
        left = 0
        right = n - 1

        num = 1
        while True:
            for i in range(left, right + 1):
                matrix[up][i] = num
                num += 1
            up += 1
            if up > down: break

            for i in range(up, down + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            if right < left: break

            for i in range(right, left - 1, -1):
                matrix[down][i] = num
                num += 1
            down -= 1
            if down < up: break

            for i in range(down, up - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            if left > right: break
        return matrix


    # 简洁不少
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix = [[0] * n for _ in range(n)]
        row, col, dirIdx = 0, 0, 0
        for i in range(n * n):
            matrix[row][col] = i + 1
            dx, dy = dirs[dirIdx]
            r, c = row + dx, col + dy
            if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] > 0:
                dirIdx = (dirIdx + 1) % 4   # 顺时针旋转至下一个方向
                dx, dy = dirs[dirIdx]
            row, col = row + dx, col + dy
        
        return matrix


S = Solution()   
re = S.generateMatrix(3)
print(re)    

