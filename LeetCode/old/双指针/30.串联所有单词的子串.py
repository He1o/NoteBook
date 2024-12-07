'''
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1：
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。

示例 2：
输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]

'''
from collections import defaultdict
class Solution:
    def findSubstring(self, s, words):
        '''
        时间复杂度 O(n)  依次判断每个单词是否符合，对于每个单词加入滑动窗口时一次，删除时一次，总计两次
                        起点不同次数是len(word),但实际每次移动指针也是len(word),因此可能是抵消了
        空间复杂度 O(m)  m是words里单词数
        '''
        ans = []
        sLen = len(s)
        wordNum = len(words)
        wordLen = len(words[0])
        wordsCnt = defaultdict(int)

        for word in words:
            wordsCnt[word] += 1

        for wordth in range(wordLen):
            windowLeft = wordth
            windowRight = wordth + wordLen * wordNum
            curWordsCnt = defaultdict(int)
            currWordLeft = windowLeft
            while windowRight <= sLen:
                currWord = s[currWordLeft : currWordLeft + wordLen]
                if currWord not in wordsCnt:
                    curWordsCnt.clear()
                    windowLeft = currWordLeft + wordLen
                    windowRight = windowLeft + wordLen * wordNum
                else:
                    curWordsCnt[currWord] += 1
                    while curWordsCnt[currWord] > wordsCnt[currWord]:
                        curWordsCnt[s[windowLeft : windowLeft + wordLen]] -= 1
                        windowLeft = windowLeft + wordLen
                        windowRight = windowRight + wordLen
                    if curWordsCnt == wordsCnt:
                        ans.append(windowLeft)
                currWordLeft += wordLen
        return ans


    # 第二次
    def findSubstring(self, s, words):
        sLen = len(s)
        wordNums = len(words)
        wordLens = len(words[0])
        tarHashMap = defaultdict(int)
        for word in words :
            tarHashMap[word] += 1
        result = []
        for startPos in range(wordLens):
            left = temp = startPos
            right = left + wordLens * wordNums
            currHashMap = defaultdict(int)
            while right <= sLen:
                currWord = s[temp:temp + wordLens]
                if currWord in tarHashMap:
                    currHashMap[currWord] += 1
                    while currHashMap[currWord] > tarHashMap[currWord]:
                        currHashMap[s[left : left + wordLens]] -= 1
                        left +=  wordLens
                        right += wordLens
                else:
                    left = temp + wordLens
                    right = left + wordLens * wordNums
                    currHashMap.clear()

                temp += wordLens
                if currHashMap == tarHashMap:
                    result.append(left)
        return result



'''
滑动窗口 + 哈希表

首先每个单词是等长的，且没有顺序要求
通过哈希表统计每个单词出现的次数
如果每个单词出现的次数相同则可以认为答案符合要求

其次通过滑动窗口来指定要判断的目标长度
滑动窗口每次前进一步，效率低，因为每前进一次，上一次的记录信息并没有保存下来
每一个窗口内的计算量是m，即words中的单词量
总时间复杂度是n*m

那可以通过每次前进一个单词的长度来提高单个滑动窗口的计算效率
每次前进一个单词，那么只需要判断新进来的单词就可以了，计算量o（1）
这时候分情况讨论
- 如果单词不在words里，滑动窗口前进到当前单词的下一个单词
- 如果单词在word里，但是数量超了，此时要将滑动窗口一个一个前进，直到数量不再超过！！
    这一点很重要，开始想的只是前进一个单词，其实当前解还不是可行解
- 不管是否符合，currwordleft前进一个单词
保证了currwordleft保持向右移动
随着每一步的移动修改滑动窗口的边界
python的截取不会超出索引
因此currwordleft是最后一个单词也无妨，因为下一个单词是''不在目标哈希表中

barfoofoobarthefoobarthe
↑        ↑
left     right
↑
curr
bar：1

barfoofoobarthefoobarthe
↑        ↑
left     right
      ↑
      curr
bar:1 foo:2

barfoofoobarthefoobarthe
   ↑        ↑
   left     right
      ↑
      curr
bar:0 foo:2

barfoofoobarthefoobarthe
      ↑        ↑
      left     right
      ↑
      curr
bar:0 foo:1

barfoofoobarthefoobarthe
      ↑        ↑
      left     right
         ↑
         curr
bar:1 foo:1

barfoofoobarthefoobarthe
      ↑        ↑
      left     right
            ↑
            curr
bar:1 foo:1 the:1  

barfoofoobarthefoobarthe
      ↑        ↑
      left     right
               ↑
               curr
bar:1 foo:2 the:1
curr会超过滑动窗口的边界，但没有关系因为超过的话一定不符合条件，会调整边界

barfoofoobarthefoobarthe
         ↑        ↑
         left     right
               ↑
               curr
bar:1 foo:1 the:1

barfoofoobarthefoobarthe
         ↑        ↑
         left     right
                  ↑
                  curr
bar:2 foo:1 the:1

barfoofoobarthefoobarthe
            ↑        ↑
            left     right
                  ↑
                  curr
bar:1 foo:1 the:1

barfoofoobarthefoobarthe
            ↑        ↑
            left     right
                     ↑
                     curr
bar:1 foo:1 the:2

barfoofoobarthefoobarthe
               ↑        ↑
               left     right 此时右边界实际超出范围但没关系，在while范围内
                     ↑
                     curr
bar:1 foo:1 the:1

barfoofoobarthefoobarthe
               ↑        ↑
               left     right 
                        ↑
                        curr
bar:1 foo:1 the:1   此时curr为''不在哈希表里

barfoofoobarthefoobarthe
                        '123'↑        ↑
                             left     right 
                        ↑
                        curr
bar:1 foo:1 the:1 
right超出范围结束循环


'''
s = "bbacaccbab"
words = ["cba","cac"]
S = Solution()   
re = S.findSubstring(s, words)
print(re)





