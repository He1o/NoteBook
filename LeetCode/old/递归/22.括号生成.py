'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]
'''
from functools import lru_cache

class Solution:
    #原版 栈的使用没有必要，可以简化
    def generateParenthesis4(self, n):
        def showmaker(right, box):
            if not right and not box:
                combinations.append(''.join(combination))
                return

            for i in range(2):
                if i ==0:
                    if right:
                        combination.append(right.pop())
                        box.append('(')
                        showmaker(right, box)
                        right.append('(')
                        combination.pop()
                        box.pop()

                else:
                    if box:
                        box.pop()
                        combination.append(')')
                        showmaker(right, box)
                        combination.pop()
                        box.append('(')

        combinations = []
        combination = []
        right = ['(' for _  in range(n)]
        box = []
        showmaker(right, box)
        return combinations

    #暴力
    def generateParenthesis3(self, n):
        def generate(A):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate([])
        return ans


    #回溯
    def generateParenthesis2(self, n):
        def backtrack(left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
            if left < n:
                S.append('(')
                backtrack(left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(left, right + 1)
                S.pop()
        
        S = []
        ans = []
        backtrack(0, 0)
        return ans

    #递归
    @lru_cache(None)
    def generateParenthesis(self, n):
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans

S = Solution()   
re = S.generateParenthesis(3)
print(re)