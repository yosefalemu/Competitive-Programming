class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()
        leftpt = 0
        ans = 0
        for rightpt in range(len(s)):
            if s[rightpt] not in set1:
                set1.add(s[rightpt])
                ans = max(ans, rightpt - leftpt + 1)
            else:
                while s[rightpt] in set1:
                    set1.remove(s[leftpt])
                    leftpt += 1
                set1.add(s[rightpt])
        return ans
