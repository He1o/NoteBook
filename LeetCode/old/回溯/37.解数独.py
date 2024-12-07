'''
编写一个程序，通过填充空格来解决数独问题。

数独的解法需 遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。

 

示例：


输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
解释：输入的数独如上图所示，唯一有效的解决方案如下所示：

'''

class Solution:
    def solveSudoku1(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(pos):
            if pos == len(spaces):
                valid[0] = True
                return
            i, j = spaces[pos]
            box_index = (i // 3) * 3 + j // 3
            for num in range(9):
                if hashmap[0][i][num] == hashmap[1][j][num] == hashmap[2][box_index][num] == 0:
                    hashmap[0][i][num] = hashmap[1][j][num] = hashmap[2][box_index][num] = 1
                    board[i][j] = str(num + 1)
                    dfs(pos + 1)
                    if valid[0]:
                        return 
                    hashmap[0][i][num] = hashmap[1][j][num] = hashmap[2][box_index][num] = 0

        hashmap = [[[0] * 9 for _ in range(9)]  for _ in range(3)]
        spaces = []
        valid = [False]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i,j))
                else:
                    num = int(board[i][j]) - 1
                    box_index = (i // 3) * 3 + j // 3
                    hashmap[0][i][num] = 1
                    hashmap[1][j][num] = 1
                    hashmap[2][box_index][num] = 1
        dfs(0)


    # 第二次
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(pos):
            if pos == len(nest):
                flag[0] = True
                return
            i, j = nest[pos]
            box_index = (i // 3) * 3 + j // 3
            for num in range(9):
                if hashmap[0][i][num] < 1 and hashmap[1][j][num] < 1 and hashmap[2][box_index][num] < 1:
                    hashmap[0][i][num] += 1
                    hashmap[1][j][num] += 1
                    hashmap[2][box_index][num] += 1
                    board[i][j] = str(num + 1)
                    backtrack(pos + 1)
                    if flag[0]:
                        return
                    hashmap[0][i][num] -= 1
                    hashmap[1][j][num] -= 1
                    hashmap[2][box_index][num] -= 1
            return

        hashmap = [[[0] * 9 for _ in range(9)]  for _ in range(3)]
        nest = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    box_index = (i // 3) * 3 + j // 3
                    hashmap[0][i][num] += 1
                    hashmap[1][j][num] += 1
                    hashmap[2][box_index][num] += 1
                else:
                    nest.append((i, j))

        flag = [False]
        backtrack(0)



    def solveSudoku(self, board):
        def flip(i: int, j: int, digit: int):
            line[i] ^= (1 << digit)
            column[j] ^= (1 << digit)
            block[i // 3][j // 3] ^= (1 << digit)

        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            
            i, j = spaces[pos]
            mask = ~(line[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
            while mask:
                digitMask = mask & (-mask)
                digit = bin(digitMask).count("0") - 1
                flip(i, j, digit)
                board[i][j] = str(digit + 1)
                dfs(pos + 1)
                flip(i, j, digit)
                mask &= (mask - 1)
                if valid:
                    return
            
        line = [0] * 9
        column = [0] * 9
        block = [[0] * 3 for _ in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    flip(i, j, digit)

        dfs(0)

'''
采用回溯的方法,在每一个点进行遍历,如果符合终极条件则返回,如果当前可以可以则进入下一层
伪代码
def
    if 是否到达最底层或者达到条件:
        return
    for  可选当前解x:
        if 是否是可行解:
            def() 进入下一个位置
            if 是否达到条件:
                return
    遍历完所有可行解自动回到上一层

对于进入下一层,可以把所有位置归纳到一起,那么进入下一层就是pos+1简化操作
否则的的话如果输入(i,j+1)到下一层,还需要在进行判断
其次需要注意的就是变量作用域,函数能够访问和使用全局变量的哪些东西
            

'''


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
S = Solution()   
re = S.solveSudoku(board)
print(board)
