class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        leftpt, rigthpt = 0, 0
        while rigthpt < len(t) and leftpt < len(s):
            if s[leftpt] == t[rigthpt]:
                leftpt += 1
            rigthpt += 1
        if leftpt == len(s):
            return True
        else:
            return False
        