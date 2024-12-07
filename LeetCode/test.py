from collections import defaultdict
from unittest import result

def func():
    def compress(s):
        n = len(s)
        for sLen in range(n // 2, 0, -1):
            maxNum = 0
            maxRes = None
            for start in range(sLen):
                res = []
                currNum = 0
                LastStr = ''
                flag = False
                for i in range(start, n, sLen):
                    if LastStr and s[i:i+sLen] == LastStr:
                        currNum += 1
                        if currNum > maxNum:
                            flag = True
                            maxNum = currNum
                            # maxStr = LastStr
                    else:
                        res.append([LastStr, currNum])
                        currNum = 0
                    LastStr = s[i:i+sLen]
                
                res.append([s[i:i+sLen], currNum])

                if flag:
                    maxRes = [[s[:start], 0]] + res[:]     

            if maxNum > 0:
                result = []
                for w, num in maxRes:
                    x = compress(w)
                    if num > 0:
                        result.append(f'{num + 1}({x})')
                    else:
                        result.append(x)
                return ''.join(result)
            
        return s


    s = input()
    print(compress(s))


if __name__ == '__main__':
    func()




