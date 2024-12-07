'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]

示例 3：
输入：nums = [0]
输出：[0]

示例 4：
输入：nums = [1]
输出：[1]
'''

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        p0, p1 = 0, len(nums) - 1
        i = 0
        while i <= p1:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                i += 1
                p0 += 1
            elif nums[i] == 2:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 -= 1
            else:
                i += 1
    '''
    保证了左边换过来的元素不会有2，右边换过来的可能是012，那么只要与右边交换完i指针不动即可
    '''

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 ,p1 = 0, 0 # 分别统计0，0+1的出现数量
        for i in range(len(nums)):
            # 先都设定成2
            buf, nums[i] = nums[i], 2
            if buf == 1 or buf == 0:
                # 设1，统计0或1是因为优先放0,0放完才放1
                nums[p1] = 1
                p1 += 1
            if buf == 0:
                # 置0在置1之后，这是因为优先放0，会有错误的1被0替换掉
                # 没被替换的就是正确的1
                nums[p0] = 0
                p0 += 1

s = [2,0,1]
S = Solution()   
re = S.sortColors(s)
print(s)    
