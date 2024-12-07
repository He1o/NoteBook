'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
'''

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''

        length = len(strs)
        count = len(strs[0])
        for i in range(count):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, length)):
                return strs[0][:i]
                
        return strs[0]

'''
1. 逻辑反向的反向还是对的，if有两种表述方式，判断对或者判断错，多想想
2. 字符串的[:0]就是空字符串''
'''


        