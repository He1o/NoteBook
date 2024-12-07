'''
题目描述
给定一个整数数组 nums和一个整数目标值 target，
请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]

进阶：你可以想出一个时间复杂度小于 O(n^2) 的算法吗？
'''

class Solution(object):
    def twoSum(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype:
        '''
        '''暴力求解'''     
        # for idx, num in enumerate(nums):
        #     print(num, idx)
        #     for i in range(idx + 1, len(nums)):
        #         if num + nums[i] == target:
        #             return [idx, i]

        '''哈希查找'''  
        # 并没有更快啊
        dct = {}
        for idx, num in enumerate(nums):
            cp =  target - num
            if cp in dct.keys():
                return [dct[cp], idx]
            else:
                dct[num] = idx

'''
暴力枚举 
时间复杂度 O(n^2),n是数组的元素数量,最坏情况下数组中每个元素被读取n次,n个数字就是n^2
空间复杂度 O(1) 不需要额外的存储空间

哈希表 
时间复杂度 O(n) 哈希表可以O(1)的寻找target - x,遍历长度n
空间复杂度 O(n) 哈希表的最大长度n  
'''

S = Solution()
result = S.twoSum([2,7,11,15], 9)
print(result)