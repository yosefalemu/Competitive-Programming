class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        i = 0
        ans = 0
        while i < len(s):
            if i + 1 < len(s) and dict1[s[i]] >= dict1[s[i + 1]]:
                ans += dict1[s[i]]
                i += 1
            elif i + 1 == len(s):
                ans += dict1[s[i]]
                i += 1
            else:
                ans += (dict1[s[i + 1]] - dict1[s[i]])
                i += 2
        return ans
                
        