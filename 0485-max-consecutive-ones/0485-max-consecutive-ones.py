class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        slowpt, fastpt = 0, 0
        ans = 0
        for c in nums:
            if c == 1:
                fastpt += 1
            else:
                slowpt = fastpt
            ans = max(ans, fastpt - slowpt)
        return ans
        
                
        