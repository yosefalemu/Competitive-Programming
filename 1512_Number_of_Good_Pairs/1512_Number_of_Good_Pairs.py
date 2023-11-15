class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1:
                count += dict1[nums[i]]
                dict1[nums[i]] += 1
            else:
                dict1[nums[i]] = 1
        return count
        
