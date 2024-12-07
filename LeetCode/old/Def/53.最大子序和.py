'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [0]
输出：0

示例 4：
输入：nums = [-1]
输出：-1

示例 5：
输入：nums = [-100000]
输出：-100000

'''

class Solution:
    # 原版
    def maxSubArray(self, nums):
        i, j = 0, 1
        result = total = nums[i]
        while j < len(nums):
            if nums[j] > 0:
                if total < 0:
                    i = j
                    total = nums[j]
                else:
                    total += nums[j]
            else:
                if nums[j] > total:
                    i = j
                    total = nums[j]
                else:
                    total += nums[j]
            result = max(result, total)
            j += 1
        return result

    # 修改1，不需要那么复杂
    # total保证了留下来的是最优的，那么当total小于0时对当前问题不会有好的结果
    def maxSubArray(self, nums):
        i, j = 0, 1
        result = total = nums[i]
        while j < len(nums):
            if total < 0:
                total = nums[j]
            else:
                total += nums[j]

            result = max(result, total)
            j += 1
        return result

    # 执行 max(nums[i] + total, nums[i]) 相当于判断total的正负号！！！
    def maxSubArray(self, nums):
        result, total = nums[0], 0
        for i in range(len(nums)):
            total = max(nums[i] + total, nums[i])
            result = max(result, total)
        return result
            




s = [-2,1,-3,4,-1,2,1,-5,4]
S = Solution()   
re = S.maxSubArray(s)
print(re)    

