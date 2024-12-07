'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

示例 1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

示例 2：
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''
from copy import deepcopy
from collections import defaultdict
class Solution:
    # 想用哈希表，动态规划的思想，做出来了但速度不大行，写的也稀烂
    def combinationSum(self, candidates, target):
        candidates.sort()
        hashmap = defaultdict(list)
        for num in candidates:
            hashmap[num].append([num])
            for key in list(hashmap.keys()):
                if key + num <= target:
                    temp = num
                    templist = deepcopy(hashmap[key])
                    while key + temp <= target:
                        for x in templist: x.append(num) 
                        y = deepcopy(templist)
                        for xx in y:
                            if xx not in hashmap[key + temp]:
                                hashmap[key + temp].append(xx)
                        temp += num
        return hashmap[target]

    # 回溯
    def combinationSum(self, candidates, target):
        combinations = []
        combination = []
        n = len(candidates)
        total = 0
        def backtrack(pos):
            nonlocal total
            if total == target:
                combinations.append(deepcopy(combination))
                return
            if total > target:
                return
            for newpos in range(pos, n):
                combination.append(candidates[newpos])
                total += candidates[newpos]
                backtrack(newpos)
                total -= candidates[newpos]
                combination.pop()
        backtrack(0)
        return combinations


    # 第二次
    def combinationSum(self, candidates, target):
        '''
        时间复杂度 O(n*2^n) 宽松的上界
        空间复杂度 O(target) 递归的栈深度最差为target层
        '''
        combination = []
        combinations = []
        total = 0
        n = len(candidates)
        def backtrack(pos):
            nonlocal total
            if total == target:
                combinations.append(combination[:])
                return
            if total > target:
                return            

            for i in range(pos, n):
                num = candidates[i]
                total += num

                combination.append(num)
                backtrack(i)
                total -= num
                combination.pop()
        
        backtrack(0)
        return combinations


'''
注意x[:]可以深层复制
不需要每次sum, total可以节省时间
'''



                    

s = [2,7,6,3,5,1]
S = Solution()   
re = S.combinationSum(s, 9)
print(re)
        

        