class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for c in s:
            if c.isalnum():
                temp += c
            else:
                continue
        ans = temp.lower()
        leftpt, rigthpt = 0, len(ans) - 1
        while leftpt <= rigthpt:
            if ans[leftpt] != ans[rigthpt]:
                return False
            leftpt += 1
            rigthpt -= 1
        return True
                
        