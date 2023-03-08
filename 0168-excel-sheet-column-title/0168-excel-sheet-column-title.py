class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            columnNumber -= 1
            ans = chr(columnNumber % 26 + 65) + ans
            columnNumber //= 26
        return ans
            
        