class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dict1 = {}
        ans = 0
        for c in nums:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1
        for c in dict1:
            if c in dict1 and c + 1 in dict1:
                ans = max(ans, (dict1[c] + dict1[c + 1]))
        return ans
        