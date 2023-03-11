class Solution:
    def reverseVowels(self, s: str) -> str:
        dict1 = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'A':1, 'E':1, 'I':1, 'O':1, 'U':1}
        tempstr = list(s)
        leftpt, rigthpt = 0, len(s) - 1
        while leftpt < rigthpt:
            if tempstr[leftpt] in dict1 and tempstr[rigthpt] in dict1:
                tempstr[leftpt], tempstr[rigthpt] = tempstr[rigthpt], tempstr[leftpt]
                leftpt += 1
                rigthpt -= 1
            elif tempstr[leftpt] in dict1:
                rigthpt -= 1
            elif tempstr[rigthpt] in dict1:
                leftpt += 1
            else:
                leftpt += 1
                rigthpt -= 1
        return "".join(tempstr)