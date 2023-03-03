class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp = set(nums)
        ans = []
        for i in range(1, len(nums) + 1):
            if i in temp:
                pass
            else:
                ans.append(i)
        return ans
        
        