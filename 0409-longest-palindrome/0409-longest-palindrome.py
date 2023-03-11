class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        isodd = False
        for c in counter:
            if counter[c] % 2 == 0:
                ans += counter[c]
            else:
                ans += (counter[c] - 1)
                isodd = True
        if isodd:
            return ans + 1
        else:
            return ans
        
            
        