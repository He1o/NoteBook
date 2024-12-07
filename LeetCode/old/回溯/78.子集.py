'''
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
输入：nums = [0]
输出：[[],[0]]
'''

class Solution:
    def subsets(self, nums):
        combination = []
        combinations = []
        n = len(nums)

        def backTrack(pos):
            combinations.append(combination[:])
            if pos >= len(nums):
                return

            for i in range(pos, n):
                combination.append(nums[i])
                backTrack(i + 1)
                combination.pop()

        backTrack(0)
            
        return combinations

s = [1,2,3]
S = Solution()   
re = S.subsets(s)
print(re)    

                