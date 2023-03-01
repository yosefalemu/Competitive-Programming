class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        dict1 = {}
        for c in range(len(nums)):
            leftpt = c + 1
            rightpt = len(nums) - 1
            target = -nums[c]
            while leftpt < rightpt:
                if nums[leftpt] + nums[rightpt] == target:
                    ans.append((nums[c], nums[leftpt], nums[rightpt]))
                    leftpt += 1 
                    rightpt -= 1
                else:
                    if nums[rightpt] + nums[leftpt] > target:
                        rightpt -= 1
                    else:
                        leftpt += 1
        for c in ans:
            if c in dict1:
                pass
            else:
                dict1[c] = 1
        return list(dict1.keys())
        
    
      
            
        
                
                
        
        