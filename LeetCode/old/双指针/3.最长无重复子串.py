'''
题目描述
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是子串的长度，"pwke" 是一个子序列，不是子串。

示例 4:
输入: s = ""
输出: 0
 '''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        '''
        时间复杂度 O(n) 
        空间复杂度 O(字符集长度)
        '''
        s = list(s)
        str_max = 0
        left = 0
        hashmap = {}
        for idx, x in enumerate(s):
            if x in hashmap.keys():
                left = max(left, hashmap[x] + 1)  #精髓，因为前一个字符可能已不在子串中，还要和left自身取一下最大值
            hashmap[x] = idx
            str_max = max(idx - left + 1, str_max)
        return str_max


    def lengthOfLongestSubstring2(self, s):
        ans = ''
        tep = ''
        for i in s:
            if i not in tep:
                tep += i
            else:
                tep = tep[tep.index(i)+1:]
                tep += i   
            if len(tep) > len(ans): 
                    ans = tep 
        return len(ans)
'''
absvxsadf
↑    ↑
absvxsadf
   ↑  ↑
滑动窗口，找到重复元素的位置，从之后开始，需要确定的是left指针的位置，且定位在后面
'''

s = 'absvxsadf'
S = Solution()   
# with timer.timer('time'):
re = S.lengthOfLongestSubstring(s)
print(re)


