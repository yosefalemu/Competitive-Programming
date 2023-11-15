class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        leftpt = 0
        rightpt = n
        while rightpt < len(nums):
            ans.append(nums[leftpt])
            ans.append(nums[rightpt])
            leftpt += 1
            rightpt += 1
        return ans
            
        
