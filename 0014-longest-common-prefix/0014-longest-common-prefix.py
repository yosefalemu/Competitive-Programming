class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        dict1 = {}
        for c in strs:
            if c in dict1:
                pass
            else:
                dict1.update({c:len(c)})
        length = min(dict1.values())
        standard = strs[0]
        ans = ""
        for i in range(length):
            for j in range(len(strs)):
                if strs[j][i] == standard[i]:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                ans += standard[i]
            else:
                break
        return ans
                
        