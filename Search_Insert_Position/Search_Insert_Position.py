class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        leftpt = 0
        rightpt = len(nums) - 1
        while leftpt <= rightpt:
            middle = (leftpt + rightpt) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                rightpt = middle - 1
            else:
                leftpt = middle + 1
        return leftpt
        


        
