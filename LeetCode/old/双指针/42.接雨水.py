'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，
可以接 6 个单位的雨水（蓝色部分表示雨水）。 

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9
'''

class Solution:
    # 双指针
    def trap(self, height):
        n = len(height)
        left = leftmax = rightmax = rain = 0
        right = n - 1

        while left <= right:
            if height[left] <= height[right]:
               rain += max(leftmax - height[left], 0)
               leftmax = max(leftmax, height[left])
               left += 1
            else:
                rain += max(rightmax - height[right], 0)
                rightmax = max(rightmax, height[right])
                right -= 1
        return rain


    # 第二次
    # 在处理的max一定是大的那一边，因为无论left或right，只要动的那一个一定是小的
    # 并且leftmax再开始已经与当前left指针指的数进行了取大的操作，因此直接操作就可以
    def trap(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        leftmax = rightmax = 0
        while left < right:
            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])
            if height[left] <= height[right]:
                result += leftmax - height[left]
                left += 1
            else:
                result += rightmax - height[right]
                right -= 1
        return result
    # 与上面相比有多余操作
    def trap(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        leftmax = rightmax = 0
        while left < right:
            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])
            if height[left] <= height[right]:
                if height[left] < min(leftmax, rightmax):
                    result += min(leftmax, rightmax) - height[left]
                left += 1
            else:
                if height[right] < min(leftmax, rightmax):
                    result += min(leftmax, rightmax) - height[right]
                right -= 1
        return result


        # 动态规划                
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans

s = [0,1,0,2,1,0,1,3,2,1,2,1]
S = Solution()   
re = S.trap(s)
print(re)
                    
        