class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.split()
        n = -1 * len(s) - 1
        for i in range(-1, n ,-1):
            if temp[i] != " ":
                return len(temp[i])
                
                
              