class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1 and abs(dict1[nums[i]] - i) <= k:
                return True
            else:
                dict1[nums[i]] = i
        return Fals
