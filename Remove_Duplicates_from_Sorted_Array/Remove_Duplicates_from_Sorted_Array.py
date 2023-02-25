class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slowpt = 0
        i = 0
        for fastpt in range(len(nums)):
            if nums[slowpt] != nums[fastpt]:
                nums[i] = nums[slowpt]
                slowpt = fastpt
                i += 1
                nums[i] = nums[fastpt]
        return i + 1
