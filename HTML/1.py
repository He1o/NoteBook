
'''
输入是由1、0组成的随机序列
变换方式： 1->0, 0->1
条件： 0后边没有1
问： 使得序列满足条件，需要的最少的变换次数；

input =   [1,0,1,1,0,0,0,1,0,1]
output = 3 #  是input变成[1,1,1,1,0,0,0,0,0,0]的次数
'''
from typing import Collection



nums = [1,0,1,1,0,0,0,1,0,1]


def sort1(nums):

    hashmapleft = {0:0, 1:0}
    hashmapright = {0:0, 1:0}
    for i in range(len(nums)):
        hashmapright[nums[i]] += 1

    result = float('inf')

    for i in range(len(nums)):
        hashmapleft[nums[i]] += 1
        hashmapright[nums[i]] -= 1

        result = min(result, hashmapleft[0] + hashmapright[1])
        
    return result

re = sort1(nums)
print(re)



