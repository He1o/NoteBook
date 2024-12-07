'''
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。


示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true

示例 3：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
'''

class Solution:
    def exist(self, board, word):
        def getnext(i, j):
            result = []
            if i > 0:
                result.append([i - 1, j])
            if j > 0:
                result.append([i, j - 1])
            if i < m - 1:
                result.append([i + 1, j])
            if j < n - 1:
                result.append([i, j + 1])
            return result

        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        flag = [False]

        def backTrack(i, j, pos):
            if board[i][j] == word[pos]:

                if pos == len(word) - 1:
                    flag[0] = True
                ne = getnext(i, j)
                for i, j in ne:
                    if not visited[i][j]:
                        if flag[0]:
                            return
                        visited[i][j] = True
                        backTrack(i, j, pos + 1)
                        visited[i][j] = False


        for i in range(m):
            for j in range(n):
                visited[i][j] = True
                backTrack(i, j, 0)
                visited[i][j] = False
                if flag[0]:
                    return True
        
        return False

    # 改进
    def exist(self, board, word):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break
            
            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        
        return False



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"


S = Solution()   
re = S.exist(board, word)
print(re)    


