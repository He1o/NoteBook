'''
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

示例 1：
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

示例 2：
输入：nums = [0]
输出：[[],[0]]

'''

class Solution:
    def subsets(self, nums):
        nums.sort()
        combination = []
        combinations = []
        n = len(nums)

        def backTrack(pos):
            combinations.append(combination[:])
            if pos >= len(nums):
                return

            for i in range(pos, n):
                if i > pos and nums[i] == nums[i - 1]:
                    continue
                combination.append(nums[i])
                backTrack(i + 1)
                combination.pop()

        backTrack(0)
            
        return combinations

s = [1,2,3]
S = Solution()   
re = S.subsets(s)
print(re)    