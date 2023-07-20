class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        dictS, dictP = {},{}
        for i in range(len(p)):
            if p[i] in dictP:
                dictP[p[i]] += 1
            else:
                dictP[p[i]] = 1
            if s[i] in dictS:
                dictS[s[i]] += 1
            else:
                dictS[s[i]] = 1
        ans = []
        l = 0
        if dictP == dictS:
            ans.append(l)
        for r in range(len(p),len(s)):
            if s[r] in dictS:
                dictS[s[r]] += 1
            else:
                dictS[s[r]] = 1
            dictS[s[l]] -= 1
            if dictS[s[l]] == 0:
                dictS.pop(s[l])
            l += 1
            if dictS == dictP:
                ans.append(l)
        return ans
