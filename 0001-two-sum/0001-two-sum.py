class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i,value in enumerate(nums):
            remaining = target - value
            if(remaining in dict1):
                return [i,dict1[remaining]]
            else:
                dict1[value] = i
        