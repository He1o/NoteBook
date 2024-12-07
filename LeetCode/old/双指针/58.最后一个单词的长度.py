'''
给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

示例 1：
输入：s = "Hello World"
输出：5

示例 2：
输入：s = " "
输出：0
'''

class Solution:
    def lengthOfLastWord(self, s):
        a = s.split()
        if a:
            return len(a[-1])
        return 0


    '''
    双指针的思想吧，我也不知道自己怎么想出来的
    一个负责指向末尾，一个负责后退
    需要考虑的是什么时候移动end和start即j
    当flag未标记时遇到空格移动end的位置
    当flag标记之后在遇到' '则跳出循环
    此时start正好指向最后一个单词开头的位置
    写的是真巧妙 哈哈哈
    '''
    def lengthOfLastWord(self, s):
        end = j = len(s) - 1

        wordflag = True
        while j >= 0:
            if s[j] == ' ' and wordflag:
                end -= 1
            elif s[j] == ' ' and not wordflag:
                break
            else:
                wordflag = False
            j -= 1
        return end - j   #s[j + 1: end + 1] 


