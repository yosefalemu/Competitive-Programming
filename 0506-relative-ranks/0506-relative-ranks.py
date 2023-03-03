class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = sorted(score, reverse=True)
        dict1 = {}
        ans = []
        for i in range(len(temp)):
            if i == 0:
                dict1.update({temp[i] : "Gold Medal"})
            elif i == 1:
                dict1.update({temp[i] : "Silver Medal"})
            elif i == 2:
                dict1.update({temp[i] : "Bronze Medal"})
            else:
                dict1.update({temp[i] : str( i + 1)})
        for c in score:
            ans.append(dict1[c])
        return ans
        
            
        
        
        