'''
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1：
输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]

示例 2：
输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

示例 3：
输入：intervals = [], newInterval = [5,7]
输出：[[5,7]]

示例 4：
输入：intervals = [[1,5]], newInterval = [2,3]
输出：[[1,5]]

示例 5：
输入：intervals = [[1,5]], newInterval = [2,7]
输出：[[1,7]]
'''

class Solution:
    def insert(self, intervals, newInterval):
        i, j = 0, len(intervals)

        while i < j:

            mid = (i + j) // 2


            if intervals[mid][0] > newInterval[0]:
                j = mid - 1
            else:
                if intervals[mid][0] <= newInterval[0] <= intervals[mid][1]:
                    break      
                i = mid + 1


    def insert(self, intervals, newInterval):
        invert = []
        left = 0
        for interval in intervals:
            if interval[1] < newInterval[0]:
                left += 1
            elif interval[0] > newInterval[1]:
                break 
            else:
                invert.append(interval)

        if invert:
            for li in invert:
                newInterval[0] = min(newInterval[0], li[0])
                newInterval[1] = max(newInterval[1], li[1])
                del intervals[left]
        intervals.insert(left, newInterval)
        
        return intervals
                

