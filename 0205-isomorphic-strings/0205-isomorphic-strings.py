class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for c1, c2 in zip(s,t):
            if c1 not in dict1 and c2 not in dict2:
                dict1[c1] = c2
                dict2[c2] = c1
            elif dict1.get(c1) != c2 or dict2.get(c2) != c1:
                return False
        return True