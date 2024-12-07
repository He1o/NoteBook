'''
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]

示例 3：
输入：nums = [1]
输出：[[1]]
'''

class Solution:
    def permute(self, nums):
        '''
        时间复杂度 O(n*n!)
        空间复杂度 O(n)

        可以使用动态数组
        
        注意:不是按顺序的
        '''
        n = len(nums)
        combination = []
        combinations = []
        def backtrack(pos):
            if pos == 0:
                combinations.append(combination[:])
                return
            for i in range(pos):
                num = nums.pop(0)
                combination.append(num)
                backtrack(pos - 1)
                nums.append(num)
                combination.pop()
        backtrack(n)        
        return combinations

    # 按大小顺序排列
    def permute(self, nums):
        n = len(nums)
        combination = []
        combinations = []
        visited = [False for _ in range(n)]
        def backtrack():
            if len(combination) == n:
                combinations.append(combination[:])
                return
            for i in range(n):
                if visited[i]:
                    continue
                combination.append(nums[i])
                visited[i] = True
                backtrack()
                combination.pop()
                visited[i] = False
        backtrack()        
        return combinations

s = [1,2,3]
S = Solution()   
re = S.permute(s)
print(re)        

