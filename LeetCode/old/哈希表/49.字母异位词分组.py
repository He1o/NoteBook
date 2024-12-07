'''
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

'''
from collections import defaultdict
class Solution:
    # 
    def groupAnagrams(self, strs):
        hashlist = []
        result = []
        for word in strs:
            hashmap = defaultdict(int)
            for letter in word:
                hashmap[letter] += 1
            for i in range(len(hashlist)):
                if hashlist[i] == hashmap:
                    result[i].append(word)
                    break
            else:
                hashlist.append(hashmap)
                result.append([word])
        return result

    '''
    想办法对目标设立相对的key值，统一编码，不要每个目标建立一个哈希表，再去比较哈希表，没有效率
    时间复杂度 O(nklog(k)) n是字符串数量，k是字符串的最大长度，需要遍历n个字符串
                        每个字符串klogk的时间进行排序，O(1)时间更新哈希表
    空间复杂度 O(nk) 需要用哈希表存储全部字符串
    '''
    def groupAnagrams(self, strs):
        mp = defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        
        return list(mp.values())


s = ["eat", "tea", "tan", "ate", "nat", "bat"]
S = Solution()   
re = S.groupAnagrams(s)
print(re)

