'''
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

示例 1：
输入：n = 3, k = 3
输出："213"

示例 2：
输入：n = 4, k = 9
输出："2314"

示例 3：
输入：n = 3, k = 1
输出："123"
'''

class Solution:
    '''原版，用的之前寻找下一排列方法'''
    def getPermutation1(self, n, k):

        numlist = [i + 1 for i in range(n)]
        temp = 1

        while temp < k:
            
            j = n - 2
            while numlist[j + 1] <= numlist[j]:
                j -= 1
            
            i = n - 1
            while numlist[i] <= numlist[j]:
                i -= 1

            numlist[j], numlist[i] = numlist[i], numlist[j]

            left, right = j + 1, n - 1
            while left < right:
                numlist[left], numlist[right] = numlist[right], numlist[left]
                left += 1
                right -= 1

            temp += 1

        return ''.join(str(x) for x in numlist)

    def getPermutation(self, n, k):
        factorial = [1]
        for i in range(1, n):
            factorial = [factorial[0] * i] + factorial

        result = []
        used = [False for _ in range(n)]
        def backTrack(k, depth):
            if len(result) == n:
                return result
            
            branch = factorial[depth]
            for i in range(n):
                if used[i]:
                    continue
                if k > branch:
                    k -= branch
                    continue
                result.append(i + 1)
                used[i] = True
                return backTrack(k, depth + 1)
        
        backTrack(k, 0)
        return ''.join(str(n) for n in result)

'''
实际是一次搜索，没有回溯的过程
更像是深度优先搜索
'''
            

        
            


S = Solution()   
re = S.getPermutation(3,3)
print(re)    