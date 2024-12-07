'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''
NUMTOSTR = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'qprs',
    '8': 'tuv',
    '9': 'wxyz',
}

class Solution:
    def letterCombinations(self, digits):
        '''
        时间复杂度 O(n^m)  n是字母长度，m是数字总个数，需要遍历每一种字母组合
        空间复杂度 O(m)  除了返回值以外，空间复杂度主要取决于哈希表以及回溯过程中的递归调用层数，
                        哈希表的大小与输入无关，可以看成常数，递归调用层数最大为m。
        '''
        if not digits:
            return []
        
        def backtrack(idx):
            if idx == n:
                combinations.append(''.join(combination))
                return
            for letter in NUMTOSTR[digits[idx]]:
                combination.append(letter)
                backtrack(idx + 1)
                combination.pop()

        n = len(digits)
        combinations = []
        combination = []
        backtrack(0)
        return combinations

'''
1. 回溯算法即深度优先算法，用于寻找所有可行解，当遇到不可行解时，舍弃不可行解并回退到上一节点
2. 递归，有递有归，先前进到最底层再将得到的结果一步步返回到上层
    递归  盗梦空间
    迭代  明日边缘
'abc'  'def'

f(0)     f(1)     f(2)
        d   →   越界返回
    ↗  
a   →   e   →   越界返回
    ↘  
        f   →   越界返回
'''