class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        slowpt = 0
        fastpt = 1
        index = 1
        while fastpt < length:
            if nums[slowpt] != nums[fastpt]:
                nums[index] = nums[fastpt]
                index += 1
                slowpt = fastpt
            fastpt += 1
        return index
       
            
            
                
                
            
        