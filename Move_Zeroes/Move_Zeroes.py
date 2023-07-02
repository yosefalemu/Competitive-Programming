class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leftpt = 0
        rightpt = 0
        n = len(nums)
        while rightpt < n:
            if nums[rightpt] != 0:
                nums[leftpt] = nums[rightpt]
                leftpt += 1
            rightpt += 1
        while leftpt < n:
            nums[leftpt] = 0
            leftpt += 1
                
        
        
