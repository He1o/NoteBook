'''

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
'''

class Solution:
    def threeSumClosest(self, nums, target):
        '''
        时间复杂度 O(n^2)，其中N是数组nums的长度。我们首先需要 O(NlogN)的时间对数组进行排序，
              随后在枚举的过程中，使用一重循环O(n)枚举a，双指针O(N)枚举b和c，故一共是 O(N^2)
        空间复杂度 O(logn)或O(n) 
        '''
        nums.sort()
        n = len(nums)
        ans = float('inf')
        for i in range(n - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1
            while j < k:
                sumthree = nums[i] + nums[j] + nums[k]
                if sumthree == target:
                    return sumthree
                elif sumthree < target:
                    if target - sumthree < abs(ans):
                        ans = sumthree - target
                    while j < k and nums[j] == nums[j + 1]:
                        j = j + 1
                    j = j + 1
                else:
                    if sumthree - target < abs(ans):
                        ans = sumthree - target
                    while j < k and nums[k] == nums[k - 1]:
                        k = k - 1
                    k = k - 1
        return ans + target

s = [-1,2,1,-4]
S = Solution()   
# with timer.timer('time'):
re = S.threeSumClosest(s,1)
print(re)