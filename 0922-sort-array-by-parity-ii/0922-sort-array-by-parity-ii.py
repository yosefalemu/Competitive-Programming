class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        evenpt, oddpt = 0, 1
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                ans[evenpt] = nums[i]
                evenpt += 2
            else:
                ans[oddpt] = nums[i]
                oddpt += 2
        return ans
            
        
        