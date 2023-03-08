class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for c in s:
            if c.isalnum():
                ans += c.lower()
            else:
                continue
        leftpt, rigthpt = 0, len(ans) - 1
        while leftpt <= rigthpt:
            if ans[leftpt] != ans[rigthpt]:
                return False
            leftpt += 1
            rigthpt -= 1
        return True
                
        