class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        slowpt = 0
        fastpt = 1
        count = 1
        index = 0
        while fastpt < length:
            if nums[slowpt] == nums[fastpt]:
                fastpt += 1
            else:
                nums[index + 1] = nums[fastpt]
                index += 1
                count += 1
                slowpt = fastpt
                fastpt += 1
        return count
       
            
            
                
                
            
        