class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count, s2Count = {}, {}
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] in s1Count:
                s1Count[s1[i]] += 1
            else:
                s1Count[s1[i]] = 1
            if s2[i] in s2Count:
                s2Count[s2[i]] += 1
            else:
                s2Count[s2[i]] = 1
        if s1Count == s2Count:
            return True
        l = 0
        for i in range(len(s1), len(s2)):
            if s2[i] in s2Count:
                s2Count[s2[i]] += 1
            else:
                s2Count[s2[i]] = 1
            s2Count[s2[l]] -= 1
            if s2Count[s2[l]] == 0:
                del s2Count[s2[l]]
            l += 1
            if s1Count == s2Count:
                return True
        return False
