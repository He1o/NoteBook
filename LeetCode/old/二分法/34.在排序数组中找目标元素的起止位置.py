'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
 

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
'''

class Solution:
    # 半二分法
    def searchRange1(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                temp1 = mid
                temp2 = mid
                while temp1 >= 0 and nums[temp1] == target:
                    temp1 -= 1
                while temp2 <= len(nums) - 1 and  nums[temp2] == target:
                    temp2 += 1
                return [temp1 + 1, temp2 - 1]
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1, -1]

    def searchRange(self, nums, target):
        left, right = 0, len(nums) - 1
        ans = [-1, -1]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                if nums[mid] == target:
                    ans[1] = mid
                left = mid + 1
                
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    ans[0] = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
'''
二分法框架不变
细节调整可以找到想要找的元素

一定要判断mid ！！！！！！！
并且带入mid+1或者mid-1
确保退出循环 ！！！！！
'''




s = [5,7,7,8,8,10]
S = Solution()   
re = S.searchRange(s, 8)
print(re)