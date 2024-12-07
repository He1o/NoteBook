'''
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

示例 2：
输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"

示例 3：
输入：s = ""
输出：0
'''
class Solution:
    # 栈
    def longestValidParentheses(self, s):
        '''
        时间复杂度 O(n) n是指定字符串的长度，只需要遍历字符串一次
        空间复杂度 O(n) 栈的大小在最坏情况下会达到n
        ''' 
        stack = [-1]
        length = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    length = i-stack[-1]
                    max_length = max(max_length,length)
        return max_length    

s = "(()"
S = Solution()   
re = S.longestValidParentheses(s)
print(re)