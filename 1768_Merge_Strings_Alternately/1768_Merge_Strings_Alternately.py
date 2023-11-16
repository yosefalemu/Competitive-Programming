class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        remainder = ""
        if len(word1) > len(word2):
            remainder = word1[len(word2):]
        if len(word1) < len(word2):
            remainder = word2[len(word1):]
        minLen = min(len(word1),len(word2))
        for i in range(minLen):
            ans += word1[i]
            ans += word2[i]
        return ans + remainder
            
