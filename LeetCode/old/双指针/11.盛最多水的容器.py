'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器。

示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例 2：
输入：height = [1,1]
输出：1

示例 3：
输入：height = [4,3,2,1,4]
输出：16

示例 4：
输入：height = [1,2,1]
输出：2
'''
class Solution:
    def maxArea(self, height):
        '''
        时间复杂度 O(n)  双指针总计遍历整个数组一次
        空间复杂度 O(1)
        '''
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res


'''
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        result = 0
        while i < j:
            result = max(result, (j - i) * min(height[i], height[j]))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return result

多了一层判断，可以省略
双指针，移动较差的位置，因为改变较好的不会让结果变得更好
'''