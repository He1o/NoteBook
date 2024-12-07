'''
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"

示例 2：
输入：s = "a", t = "a"
输出："a"
'''

from collections import defaultdict
class Solution:
    def minWindow(self, s, t):
        hashmap = defaultdict(int)
        for letter in t:
            hashmap[letter] += 1
        cnt = sum(hashmap.values())
        left = right = 0
        result = ''
        while right < len(s):
            while cnt > 0 and right < len(s):
                if s[right] in hashmap:
                    hashmap[s[right]] -= 1
                    if hashmap[s[right]] >= 0:
                        cnt -= 1
                right += 1

            while cnt == 0:
                if s[left] in hashmap:
                    hashmap[s[left]] += 1
                    if hashmap[s[left]] > 0:
                        cnt += 1
                if not result or (right - left) < len(result):
                    result = s[left:right]
                left += 1

        return result

s = "cabwefgewcwaefgcf"
t = "cae"

S = Solution()   
re = S.minWindow(s,t)
print(re)    
