'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"

示例 2:
输入: num1 = "123", num2 = "456"
输出: "56088"

说明：
num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
'''

class Solution:
    # 原版
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        numlist = []
        for i in range(len(num1) - 1, -1, -1):
            s = ['0'] * (len(num1) - 1 - i)
            n1 = int(num1[i])
            pre = 0
            for j in range(len(num2) - 1, -1, -1):
                n2 = int(num2[j])
                x = (n1 * n2) % 10 + pre
                pre = (n1 * n2) // 10
                s = [str(x)] + s
            if pre:
                s = [str(pre)] + s
            numlist.append(s)

        result = ''
        pre = 0
        while numlist or pre:
            add = 0

            for num in numlist:
                x = num.pop()
                add += int(x)
            while [] in numlist:
                numlist.remove([])

            add += pre
            
            pre = add // 10
            result = str(add % 10) + result
        return result

    # 改进
    # 每次都进行累加，最后就不用一起处理了
    # 把复杂的问题简单化！！！
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        
        ans = "0"
        m, n = len(num1), len(num2)
        for i in range(n - 1, -1, -1):
            add = 0
            y = int(num2[i])
            curr = ["0"] * (n - i - 1)
            for j in range(m - 1, -1, -1):
                product = int(num1[j]) * y + add
                curr.append(str(product % 10))
                add = product // 10
            if add > 0:
                curr.append(str(add))
            curr = "".join(curr[::-1])
            ans = self.addStrings(ans, curr)
        
        return ans
    
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        add = 0
        ans = list()
        while i >= 0 or j >= 0 or add != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            result = x + y + add
            ans.append(str(result % 10))
            add = result // 10
            i -= 1
            j -= 1
        return "".join(ans[::-1])


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        ansArr = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            for j in range(n - 1, -1, -1):
                ansArr[i + j + 1] += x * int(num2[j])
        
        for i in range(m + n - 1, 0, -1):
            ansArr[i - 1] += ansArr[i] // 10
            ansArr[i] %= 10
        
        index = 1 if ansArr[0] == 0 else 0
        ans = "".join(str(x) for x in ansArr[index:])
        return ans

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i+j
                p2 = i + j + 1
                sum_ = res[p2] + mul
                res[p2] = sum_ % 10
                res[p1] += sum_ // 10

        for i in range(len(res)):    # 去除res前面的0
            if res[i] != 0:
                break
        res = [str(v) for v in res[i:]]

        return "".join(res)

num1 = "123"
num2 = "456"
S = Solution()   
re = S.multiply(num1, num2)
print(re)