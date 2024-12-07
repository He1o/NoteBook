'''
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        n = len(nums)
        combination = []
        combinations = []
        def backtrack(pos):
            if pos == 0:
                combinations.append(combination[:])
                return
            pre = None
            for i in range(pos):
                num = nums.pop(0)
                combination.append(num)
                if num != pre:
                    backtrack(pos - 1)
                    pre = num
                nums.append(num)
                combination.pop()
        backtrack(n)        
        return combinations

s = [1,1,3]
S = Solution()   
re = S.permuteUnique(s)
print(re)        
