'''
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须 原地 修改，只允许使用额外常数空间。

示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]

示例 3：
输入：nums = [1,1,5]
输出：[1,5,1]

示例 4：
输入：nums = [1]
输出：[1]

'''
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = n - 1
        while j >= 0:
            i = j - 1
            if i >=0 and nums[j] > nums[i]:
                left = i
                for k in range(n - 1, j - 1, -1):
                    if nums[i] < nums[k]:
                        j = k
                        right = j
                        break
                nums[left], nums[right] = nums[right], nums[left]
                break
            j -= 1
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # 第二次
    def nextPermutation(self, nums):
        '''
        时间复杂度 O(n) n为给定序列的长度，至多扫描序列两遍，以及进行一次翻转操作
        空间复杂度 O(1)
        '''
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                j = n - 1
                while nums[j] <= nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                reverse(i + 1, n - 1)
                return
            i -= 1

        reverse(0, n - 1)


'''
首先一定是要移动或交换
为了使数值只是增大一点，
就是让右边'较大值'能够放到前面去，而这个较大值要尽可能的小，指的是数字小
同时使左边'较小值'放到后面去，这个较小值要尽可能的靠后，指的是位置尽可能靠右
开始想i指针不动，j指针倒退，直到找到j<i
但这种思路不对，因为想要找到的尽可能j靠右的可交换值，所以ji应该同时移动，找到j<i
因为只要j>i已走过的位置无论怎么交换数都不会变大
这样遍历过的地方，保证了i及右边的所有数都是降序排列
              j i
1 9 8 4 7 6 5 3 1
      j i
1 9 8 4 7 6 5 3 1

此时因为j>i交换两者会使数变大，但为了保证i尽可能小，同时还要i比j大
将i从最右边再次遍历，找到比j大的那个值
      j     i
1 9 8 4 7 6 5 3 1
交换ij的值，还是保证了i及右边的所有数都是降序排列
      j     i
1 9 8 5 7 6 4 3 1
将j后面的数重置为升序即为最小的排列
      j     i
1 9 8 5 1 3 4 6 7
'''
    
s = [2,3,1,3,3]
S = Solution()   
# with timer.timer('time'):
re = S.nextPermutation(s)
print(s)




