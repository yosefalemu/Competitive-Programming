class Solution:
    def frequencySort(self, s: str) -> str:
        tempDict = {}
        ans = ""
        for c in s:
            if c in tempDict:
                tempDict[c] += 1
            else:
                tempDict[c] = 1
        sorted_dict = dict(sorted(tempDict.items(), key=lambda x: x[1], reverse=True))
        for c in sorted_dict:
            for i in range(0,sorted_dict[c]):
                ans += c
        return ans
                