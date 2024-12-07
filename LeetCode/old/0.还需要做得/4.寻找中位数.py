'''
题目描述
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出并返回这两个正序数组的中位数 。

示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

示例 3：
输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000

示例 4：
输入：nums1 = [], nums2 = [1]
输出：1.00000

示例 5：
输入：nums1 = [2], nums2 = []
输出：2.00000

要求时间复杂度为 O(log (m+n))
'''



class Solution(object):
    # 第一次
    def findMedianSortedArrays1(self, nums1, nums2):
        '''
        时间复杂度 O(log(m+n)) 初始时k = (m + n)/2 每一轮循环可以将查找范围减少一半
        空间复杂度 O(1)
        '''
        def getK(k):
            i1 = p1 = 0
            i2 = p2 = 0
            ans = []
            while True:
                a = k // 2 

                if i1 == m:
                    return nums2[i2 + k - 1]
                if i2 == n:
                    return nums1[i1 + k - 1]
                if k == 1:
                    return  min(nums1[i1], nums2[i2])

                ap1 = min(m, a)
                ap2 = min(n, a)
                p1 = i1 + ap1 - 1
                p2 = i2 + ap2 - 1


                if nums1[p1] < nums2[p2]:
                    i1 = i1 + ap1
                    k = k - ap1
                else:
                    i2 = i2 + ap2
                    k = k - ap2

        m = len(nums1)        
        n = len(nums2)
        k = (m + n + 1) // 2
        if (m + n) % 2 == 1:
            ans = getK(k)
        else:
            ans = (getK(k) + getK(k + 1)) / 2
        return ans

    # 第二次
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        k = (n + m + 1) // 2
        def getK(i, j, k):
            if i == n: return nums2[j + k - 1]
            if j == m: return nums1[i + k - 1]
            if k == 1:
                return min(nums1[i], nums2[j])
            pos = k // 2 - 1
            pos = min(m - 1, pos)
            pos = min(n - 1, pos)
            if nums1[i + pos] <= nums2[j + pos]:
                return getK(i + pos + 1, j, k - pos - 1)
            else:
                return getK(i, j + pos + 1, k - pos - 1)
        if (m + n) % 2 == 0:
            return (getK(0, 0, k) + getK(0, 0, k + 1)) / 2
        else:
            return getK(0, 0, k)
'''
二分法的原理
1. 长度m和n的数组，要找到中位数，需要找到第 (m + n + 1) // 2 个数，等同向下取整
2. 假设要找第y个数，先定位每个数组的第x个数，比较两个数的大小，可以确定较大的那个数最多有2x-1个数比它小
而第y个数则有y-1个数比其小，因此为了保证中位数不被剔除，2x-1<=y-1  x最大可以取 y//2
3. 指针前进，剔除几个数就指向下一个数，同时因为剔除了x个数，因此k=k-x
4. 为了保证x不大于数组长度，还需要min(m,x),同时k减去其值
5. 最后特殊情况，当一个数组被剔除干净时，找的就是另一个数组的第k个值
    k=1时，输出两个数组第一个数的最小值即可，因为k=1即为找第一小的数


1 2 4 5 [5] 7 7 8 9 9
1 4 5 7 9   k = 5  x = 2   //为什么不能是3，当x = 3时，则最多有5个数比保留的那个较大的数小，那它有可能是老六
  ↑
2 5 7 8 9
  ↑

[1 4] 5 7 9   k = 3  x = 1
      ↑
2 5 7 8 9
↑

[1 4] 5 7 9   k = 2  x = 1
      ↑
[2] 5 7 8 9
    ↑

[1 4 5] 7 9   k = 1  
        ↑
[2] 5 7 8 9
    ↑

时间复杂度 log(m + n)
'''

a = [1]
b = [2, 3, 4, 5, 6]
S = Solution()   
# with timer.timer('time'):
re = S.findMedianSortedArrays(a, b)
print(re)