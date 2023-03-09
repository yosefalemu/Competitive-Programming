class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        digit = 0
        position = 0
        ans = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            digit = ord(columnTitle[i]) - 64
            ans += digit*(26**position)
            position += 1
        return ans
        