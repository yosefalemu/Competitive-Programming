class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        leftpt, rightpt,count = 0, 0, 0
        while leftpt < len(g) and rightpt < len(s):
            if s[rightpt] >= g[leftpt]:
                leftpt += 1
            rightpt += 1
        return leftpt
        