'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：答案中不可以包含重复的四元组。

示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：
输入：nums = [], target = 0
输出：[]
'''

class Solution:
    def fourSum(self, nums, target):
        '''
        时间复杂度 O(n^3 + nlogn) = O(n^3)
        '''
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue

                k = j + 1
                h = n - 1
                while k < h:
                    print(i, j, k, h)
                    sumfour = nums[i] + nums[j] + nums[k] + nums[h]
                    if sumfour == target:
                        ans.append([nums[i], nums[j], nums[k], nums[h]])
                        while k < h and nums[k] == nums[k + 1]:
                            k = k + 1
                        while k < h and nums[h] == nums[h - 1]:
                            h = h - 1
                        k = k + 1
                        h = h - 1
                    elif sumfour < target:
                        k = k + 1
                    else:
                        h = h - 1
        return ans

s = [1,0,-1,0,-2,2]
S = Solution()   
# with timer.timer('time'):
re = S.fourSum(s, 0)
print(re)



