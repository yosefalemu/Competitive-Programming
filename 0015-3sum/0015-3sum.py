class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for c in range(len(nums) - 2):
            if c > 0 and nums[c] == nums[c-1]:
                continue
            leftpt = c + 1
            rightpt = len(nums) - 1
            while leftpt < rightpt:
                sum = nums[c] + nums[leftpt] + nums[rightpt]
                if sum == 0:
                    ans.append((nums[c], nums[leftpt], nums[rightpt]))
                    while leftpt < rightpt and nums[leftpt] == nums[leftpt + 1]:
                        leftpt += 1
                    while leftpt < rightpt and nums[rightpt] == nums[rightpt-1]:
                        rightpt -= 1
                    leftpt += 1 
                    rightpt -= 1
                else:
                    if sum > 0:
                        rightpt -= 1
                    else:
                        leftpt += 1
        return ans
      
            
        
                
                
        
        