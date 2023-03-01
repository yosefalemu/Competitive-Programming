class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        list1 = []
        ans = {}
        for c in range(len(nums)):
            leftpt = c + 1
            rightpt = len(nums) - 1
            target = -nums[c]
            while leftpt < rightpt:
                if nums[leftpt] + nums[rightpt] == target:
                    list1.append((nums[c], nums[leftpt], nums[rightpt]))
                    leftpt += 1 
                    rightpt -= 1
                else:
                    if nums[rightpt] + nums[leftpt] > target:
                        rightpt -= 1
                    else:
                        leftpt += 1
        for c in list1:
            if c in ans:
                pass
            else:
                ans[c] = 1
        return list(ans.keys())
        
    
      
            
        
                
                
        
        