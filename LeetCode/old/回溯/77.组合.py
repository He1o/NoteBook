'''
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''

class Solution:
    def combine(self, n, k):
        combination = []
        combinations = []


        def backTrack(pos):
            if len(combination) == k:
                combinations.append(combination[:])
                return

            for i in range(pos, min(n, n - k + 1 + pos)):
                combination.append(i + 1)
                backTrack(i + 1)
                combination.pop()

        backTrack(0)
        return combinations

S = Solution()   
re = S.combine(4, 2)
print(re)    

                



        
