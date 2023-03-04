class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                ans += nums[i]
        return ans
            
        