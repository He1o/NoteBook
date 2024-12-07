'''
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

 示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution:
    def spiralOrder(self, matrix):
        up = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        result = []

        while True:
            for i in range(left, right + 1, 1):
                result.append(matrix[up][i])
            up += 1
            if up > down: break

            for i in range(up, down + 1, 1):
                result.append(matrix[i][right])
            right -= 1
            if right < left: break

            for i in range(right, left - 1, -1):
                result.append(matrix[down][i])
            down -= 1
            if down < up: break

            for i in range(down, up - 1, -1):
                result.append(matrix[i][left])
            left += 1
            if left > right: break
        
        return result