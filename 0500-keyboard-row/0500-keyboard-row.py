class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        string1 = list("qwertyuiop")
        string2 = list("asdfghjkl")
        string3 = list("zxcvbnm")
        ans = []
        
        
        for eachword in words:
            flag = 0
            word = eachword.lower()
            if word[0] in string1:
                temp = string1
            elif word[0] in string2:
                temp = string2
            else:
                temp = string3
            for c in word:
                if c not in temp:
                    flag = 1
                    break
            if flag == 0:
                ans.append(eachword)
        return ans
            
        
        