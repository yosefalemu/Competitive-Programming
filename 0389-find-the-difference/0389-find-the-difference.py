class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter1 = Counter(s)
        counter2 = Counter(t)
        for c in counter2:
            if c not in counter1 or counter2[c] != counter1[c]:
                return c
        