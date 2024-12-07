'''
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，
使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，
则返回它的下标，否则返回 -1 。

示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

示例 2：
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

示例 3：
输入：nums = [1], target = 0
输出：-1

'''

class Solution:
    # 原版
    '''    
    def search(self, nums, target):
        def orderSearch(left, right):
            if left == right and nums[left] != target:
                return -1
            if nums[left] == target:
                return left
            mid = (left + right) // 2
            if target <= nums[mid]:
                return orderSearch(left, mid)
            else:
                return orderSearch(mid + 1, right)

        def unorderSearch(left, right):
            if left == right and nums[left] != target:
                return -1
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    return orderSearch(left, mid)
                else:
                    return unorderSearch(mid + 1, right)
            else:
                if nums[mid + 1] <= target <= nums[right]:
                    return orderSearch(mid + 1, right)
                else:
                    return unorderSearch(left, mid)
        return unorderSearch(0, len(nums) - 1)
    '''

    # 第二次
    def search(self, nums, target):
        '''
        时间复杂度 O(logn) n为数组的大小
        空间复杂度 O(1) 
        '''
        def Bisection(i, j):
            if nums[i] == target:
                return i
            if i == j:
                return -1

            mid = (i + j) // 2
            if nums[i] <= nums[mid]:
                if nums[i] <= target <= nums[mid]:
                    return Bisection(i, mid)
                else:
                    return Bisection(mid + 1, j)
            else:
                if nums[mid] < target <= nums[j]:
                    return Bisection(mid + 1, j)
                else:
                    return Bisection(i, mid)
        return Bisection(0, len(nums) - 1)

    # 最好写成这个样子
    # 判断mid的值，无论如何mid前进或后退，必定退出循环
    def search(self, nums, target):
        def Bisection(i, j):
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if i == j:
                return -1 
           
            if nums[i] <= nums[mid]:
                if nums[i] <= target < nums[mid]:
                    return Bisection(i, mid - 1)
                else:
                    return Bisection(mid + 1, j)
            else:
                if nums[mid] < target <= nums[j]:
                    return Bisection(mid + 1, j)
                else:
                    return Bisection(i, mid - 1)
        return Bisection(0, len(nums) - 1)


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1





s = [5,1,3]
S = Solution()   
re = S.search(s, 1)
print(re)
