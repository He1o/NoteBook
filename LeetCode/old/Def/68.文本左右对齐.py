

class Solution:
    def fullJustify(self, words, maxWidth):
        roWords = []
        totalWords = []
        totalCnt = []

        wlen = 0
        for w in words:
            if wlen + len(w) > maxWidth:
                totalCnt.append(wlen - len(roWords))
                totalWords.append(roWords)
                wlen = 0
                roWords = []
            wlen += len(w) + 1
            roWords.append(w)
        if roWords:
            totalCnt.append(wlen - 1)
            totalWords.append(roWords)

        result = []
        for i in range(len(totalWords) - 1):
            spaces = maxWidth - totalCnt[i]
            wordCnt = len(totalWords[i]) - 1
            if wordCnt:
                eachSpaces = spaces // wordCnt 
                surPlus = spaces % wordCnt 
                context = ''
                for w in totalWords[i][:-1]:
                    context += w
                    context += ' ' * eachSpaces
                    if surPlus:
                        context += ' '
                        surPlus -= 1
                context += totalWords[i][-1]
                result.append(context)
            else:
                context = totalWords[i][0]
                context += ' ' * spaces
                result.append(context)

        result.append(' '.join(totalWords[-1]) + ' '*(maxWidth -  totalCnt[-1]))
        return result

s = ["What","must","be","acknowledgment","shall","be"]
S = Solution()   
re = S.fullJustify(s, 16)
print(re)    