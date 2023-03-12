class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        i = len(s) - 1
        ans = ""
        count = 0
        while i >= 0:
            if count < k and s[i] != "-":
                ans = s[i] + ans
                count += 1
                i -= 1
            elif count == k:
                ans = "-" + ans
                count = 0
            else:
                i -= 1
        if (len(ans) > 0 and ans[0] == '-'):
            ans = ans[1:]
        return ans
            