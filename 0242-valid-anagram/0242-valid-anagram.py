class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for c1 in s:
            if c1 in dict1:
                dict1[c1] += 1
            else:
                dict1[c1] = 1
        for c2 in t:
            if c2 in dict2:
                dict2[c2] += 1
            else:
                dict2[c2] = 1
        if dict1 == dict2:
            return True
        else:
            return False
        