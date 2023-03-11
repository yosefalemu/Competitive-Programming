class Solution:
    def firstUniqChar(self, s: str) -> int:
        tempDict = Counter(s)
        for i in range(len(s)):
            if tempDict[s[i]] == 1:
                return i
        return -1
        