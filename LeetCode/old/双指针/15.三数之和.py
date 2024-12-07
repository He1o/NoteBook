'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。


示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]
'''

class Solution:
    def threeSum(self, nums):
        '''
        时间复杂度 O(n^2) 
        空间复杂度 O(n)  排序需要额外的存储空间
        '''
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 2):
            if nums[i] > 0:
                return ans
            if i and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            target = -nums[i]
            while j < k:
                if nums[j] > target:  # 剪枝  如果大于目标值，表示无论如何都无法满足
                    break
                if nums[j] + nums[k] == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j = j + 1
                    while j < k and nums[k] == nums[k - 1]:
                        k = k - 1
                    j = j + 1
                    k = k - 1
                elif nums[j] + nums[k] > target:
                    k = k - 1
                else:
                    j = j + 1
        return ans

    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        ans = list()
        
        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans

'''
暴力求解有三重循环枚举每一种可能，复杂且重复
1. 首先排序，对于有序数组有些算法才可以使用
2. 去除重复的本质，即保证下一重循环的开始不大于当前循环，且任一循环的指针移动时应跳过相同元素
2. 当我们需要枚举数组中的两个元素时，如果我们发现随着第一个元素的递增，第二个元素是递减的，
那么就可以使用双指针的方法，将枚举的时间复杂度从 O(N^2)减少至 O(N)。
可以发现在本问题中，当第一个指针确定，j指针右移会使和变大，k指针左移会使值变小
因此判断三者之和来移动jk指针，
当sum==0:同时移动jk，且保证j<k并与移动之前没有重复元素
当sum<0:移动j，使sum的值变大
当sum>0:移动k，使sum的值变小
3, 0, -2, -1, 2, 2
↑  ↑             ↑
i  j             k


3, 0, -2, -1, 2, 2
↑      ↑   ↑
i      j   k
'''
        

s = [3,0,-2,-1,1,2]
S = Solution()   
# with timer.timer('time'):
re = S.threeSum1(s)
print(re)
                    
