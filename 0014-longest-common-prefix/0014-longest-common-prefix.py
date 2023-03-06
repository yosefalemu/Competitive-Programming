class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        dict1 = {}
        for c in strs:
            if c in dict1:
                pass
            else:
                dict1.update({c:len(c)})
        length = min(dict1.values())
        base = strs[0]
        ans = ""
        for i in range(length):
            for j in range(len(strs)):
                if strs[j][i] == base[i]:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                ans += base[i]
            else:
                break
        return ans
                
        