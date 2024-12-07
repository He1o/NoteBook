'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

假设你总是可以到达数组的最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

示例 2:
输入: [2,3,0,1,4]
输出: 2
'''

class Solution:

    def jump(self, nums):
        if len(nums) == 1:
            return 0
        step = curr = 0
        while curr < len(nums) - 1:
            num = nums[curr]
            maxstep =0
            for i in range(1, num + 1):
                if i + curr == len(nums) - 1:
                    return step + 1
                if i + nums[curr + i] > maxstep:
                    maxstep = i + nums[curr + i]
                    nextstep = i + curr
            step += 1
            curr = nextstep



    def jump(self, nums):
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
