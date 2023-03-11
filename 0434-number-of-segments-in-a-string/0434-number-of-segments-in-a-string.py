class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if (i == 0 or s[i - 1] == " ") and s[i] != " ":
                count += 1
        return count
        
        