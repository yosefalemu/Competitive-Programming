class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        leftpt, rigthpt = 0, len(s) - 1
        while leftpt < rigthpt:
            temp = s[leftpt]
            s[leftpt] = s[rigthpt]
            s[rigthpt] = temp
            leftpt += 1
            rigthpt -= 1
        