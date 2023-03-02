class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        count = 1
        slowpt = 0
        for fastpt in range(1, len(nums)):
            if nums[slowpt] != nums[fastpt]:
                slowpt = fastpt
                count += 1
            if count == 3:
                return nums[slowpt]
        return nums[0]
                
            
            
            
        