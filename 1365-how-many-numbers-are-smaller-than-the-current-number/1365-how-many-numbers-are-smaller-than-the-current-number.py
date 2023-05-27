class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(0, n):
            count = 0
            for j in range(0, n):
                if i != j and nums[j] < nums[i]:
                    count += 1
            ans.append(count)
        return ans
        
        