class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slowpt, fastpt = 0, 0
        for fastpt in range(len(nums)):
            if nums[slowpt] == 0 and nums[fastpt] != 0:
                temp = nums[slowpt]
                nums[slowpt] = nums[fastpt]
                nums[fastpt] = temp
                slowpt += 1
            fastpt += 1
            if nums[slowpt] != 0:
                slowpt += 1
                
        