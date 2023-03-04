class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        set1 = set(candyType)
        return min(len(set1), len(candyType)//2)
            
        