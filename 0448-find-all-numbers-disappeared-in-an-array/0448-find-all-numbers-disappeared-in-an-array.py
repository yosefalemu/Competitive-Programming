class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp = [False] * (len(nums) + 1)
        ans = []
        for i in nums:
            temp[i] = True
        for i in range(1, len(temp)):
            if temp[i]:
                pass
            else:
                ans.append(i)
        return ans
        
        
        