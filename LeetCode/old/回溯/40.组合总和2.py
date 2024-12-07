'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
'''

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        total = 0
        combination = []
        combinations = []
        def backtrack(pos):
            nonlocal total
            if total == target:
                combinations.append(combination[:])
                return
            num = None
            for i in range(pos, n):
                if candidates[i] == num:
                    continue
                num = candidates[i]
                total += num
                if total > target:
                    total -= num
                    return
                combination.append(num)
                backtrack(i + 1)
                combination.pop()
                total -= num
        backtrack(0)
        return combinations
    '''
    如何避免重复
    在for循环中跳过重复的元素
    我为什么没想出来呢
    '''

    # 第二次
    def combinationSum2(self, candidates, target):
        candidates.sort()
        combination = []
        combinations = []
        total = 0
        n = len(candidates)
        def backtrack(pos):
            nonlocal total
            if total == target:
                combinations.append(combination[:])
                return
       
            pre = None
            for i in range(pos, n):
                num = candidates[i]
                if num == pre:
                    continue
                pre = num
                total += num
                if total > target:
                    total -= num
                    return     
                combination.append(num)
                backtrack(i + 1)
                combination.pop()
                total -= num
        
        backtrack(0)
        return combinations

    # 修改
    def combinationSum2(self, candidates, target):
        def dfs(begin, residue):
            if residue == 0:
                combinations.append(combination[:])
                return

            for index in range(begin, size):
                if candidates[index] > residue:
                    break
                if index > begin and candidates[index - 1] == candidates[index]:
                    continue
                combination.append(candidates[index])
                dfs(index + 1, residue - candidates[index])
                combination.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        combinations = []
        combination = []
        dfs(0, target)
        return combinations


s = [10,1,2,7,6,1,5]
S = Solution()   
re = S.combinationSum2(s, 8)
print(re)
        