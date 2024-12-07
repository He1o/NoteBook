'''
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

示例 1：
输入：nums = [1,2,0]
输出：3

示例 2：
输入：nums = [3,4,-1,1]
输出：2

示例 3：
输入：nums = [7,8,9,11,12]
输出：1
。
'''

class Solution:
    # 用enumerate
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = -num + n + 1
        for i, num in enumerate(nums):
            num = abs(num)
            if num <= n and nums[num - 1] > 0:
                nums[num - 1] = -nums[num - 1]        
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        return n + 1


    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


s = [10,1,2,7,6,1,5]
S = Solution()   
re = S.firstMissingPositive(s)
print(re)
        
        
