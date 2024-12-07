'''

实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置
（下标从 0 开始）。如果不存在，则返回  -1 。

说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

示例 1：
输入：haystack = "hello", needle = "ll"
输出：2

示例 2：
输入：haystack = "aaaaa", needle = "bba"
输出：-1

示例 3：
输入：haystack = "", needle = ""
输出：0
'''



class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        
        i, j = 0, len(needle)
        while j <= len(haystack):
            if haystack[i:j] == needle:
                return i
            i += 1
            j += 1
        return -1
    
    # KMP算法
    def strStr(self, haystack, needle):
        m = len(haystack)
        n = len(needle)
        if not needle:
            return 0
        if m < n:
            return -1
        
        Pmt = [0]
        i = 0
        j = 1
        while j < n:
            if needle[j] == needle[i]:
                Pmt.append(i + 1)
                i += 1
                j += 1
            elif i == 0:
                Pmt.append(0)
                j += 1
            else:
                i = Pmt[i - 1]

        i = 0
        j = 0
        while j < m:
            if haystack[j] == needle[i]:
                i += 1
                j += 1
                if i == n:
                    return j - n
            elif i == 0:
                j += 1
            else:
                i = Pmt[i - 1]
        return -1


'''
KMP算法分为两部分

第一部分求pmt部分匹配表
PMT中的值是字符串的前缀集合与后缀集合的交集中最长元素的长度
 j=1
aabaaf
 aabaaf
 i=0
01

 j=1
aabaaf
 aabaaf
  i=1
01


  j=2
aabaaf
  aabaaf
  i=0
010


   j=3
aabaaf
   aabaaf
   i=0
0101
   ↑
   i+1

    j=4
aabaaf
   aabaaf
    i=1
01012
    ↑
    i+1


     j=5
aabaaf
   aabaaf
     i=2
01012

     j=5
aabaaf
    aabaaf
     i=pmt(i-1)=1
01012

aabaaf
     aabaaf
     i=pmt(i-1)=0
010120

有点类似动态规划的思想
我开始想的是相同的话ij都后移一位，这点没有问题
如果不同则该点pmt为0，j后移一位，i=0，这点就有问题了
尽管当前ij的值不同不代表j与i前面的每一位都不同，最起码j还应该i=0进行比较
尽管这样还是会漏掉j前面已经有匹配的元素
那i应该返回到哪一位？
可以假设i前面还有i-1位元素，可以确定的是这些元素与j前面同数量的元素是匹配的
而这些元素的最大相同前后缀就是pmt[i-1]
因此让i=pmt[i-1]就是让i回退到前面i-1个元素的最大相同前后缀
当i=0时与j元素还不匹配，则j后移一位

有了目标pmt表
j在原字符串上移动
同理
注意j和i都是从0开始
且判断i==n说明完全匹配返回j-n
'''


haystack = "aabaabaafa"
needle = "aabaaf"
S = Solution()   
re = S.strStr(haystack, needle)
print(re)