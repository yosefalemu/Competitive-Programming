class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        dict1 = {}
        for c in nums:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1
        for key, value in dict1.items():
            if value > len(nums)/2:
                return key
