class Solution:
    def intToRoman(self, s):
        '''
        时间复杂度 O(n) 
        空间复杂度 O(1)
        '''
        Romanlists = {
            'M' :  1000,
            'CM':  900 ,
            'D' :  500 ,
            'CD':  400 , 
            'C' :  100 ,
            'XC':  90  ,
            'L' :  50  ,
            'XL':  40  ,
            'X' :  10  ,
            'IX':  9   ,
            'V' :  5   ,
            'IV':  4   ,
            'I' :  1   ,
        }
        num = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in Romanlists:
                num = num + Romanlists[s[i:i+2]]
                i = i + 2
            else:
                num = num + Romanlists[s[i]]
                i = i + 1
        return num

s = 'XCIV'
S = Solution()   
# with timer.timer('time'):
re = S.intToRoman(s)
print(re)

