'''
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
'''

class Solution:
    def canJump(self, nums):
        right = 0
        for i in range(len(nums)):
            if i <= right:
                right = max(right, i + nums[i])
            else:
                return False

        return True

    # 改进
    # 当最远点大于等于终点，即可返回True，不用遍历到末尾
    def canJump(self, nums):
        n, right = len(nums), 0
        for i in range(n):
            if i <= right:
                right = max(right, i + nums[i])
                if right >= n - 1:
                    return True
            else:
                return False

    # 避免用max会更快一点
    def canJump(self, nums):
        n, right = len(nums), 0
        for i in range(n):
            if i <= right:
                right = right if right >= i + nums[i] else i + nums[i]
                if right >= n - 1:
                    return True
            else:
                return False
