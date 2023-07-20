class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        intSum = 0
        l = 0
        for r in range(len(nums)):
            intSum += nums[r]
            while intSum >= target:
                ans = min(ans,r - l + 1)
                intSum -= nums[l]
                l += 1
        if ans < float("inf"):
            return ans
        else:
            return 0
                
            
        
        
