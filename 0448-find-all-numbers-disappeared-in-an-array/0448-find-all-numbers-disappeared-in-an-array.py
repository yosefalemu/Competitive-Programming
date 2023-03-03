class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dict1 = {}
        ans = []
        for c in nums:
            if c in dict1:
                pass
            else:
                dict1[c] = 1
        for i in range(1, len(nums) + 1):
            if i in dict1:
                pass
            else:
                ans.append(i)
        return ans
        
        