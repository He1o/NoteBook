'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
'''

class Solution:
    def searchInsert(self, nums, target):

        ans = len(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    # 第二次
    # 神了，连ans都不用了，速度最快
    def searchInsert(self, nums, target):
        '''
        时间复杂度 O(logn)
        空间复杂度 O(1)
        '''
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

'''
ans值设为数组长度可以省去边界条件判断
'''


s = [1,3,5,6]
S = Solution()   
re = S.searchInsert(s, 0)
print(re)
        

        
        