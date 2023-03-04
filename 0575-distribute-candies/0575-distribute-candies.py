class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        candyType.sort()
        ans = 1
        slowpt, fastpt = 0, 0
        while ans < n/2 and fastpt < n:
            if candyType[slowpt] != candyType[fastpt]:
                ans += 1
                slowpt = fastpt
            fastpt += 1
        return ans
            
        