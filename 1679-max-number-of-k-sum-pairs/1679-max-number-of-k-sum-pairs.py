class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        leftpt = 0
        rightpt = len(nums) - 1
        ans = 0
        while leftpt < rightpt:
            if nums[leftpt] + nums[rightpt] < k:
                leftpt += 1
            elif nums[leftpt] + nums[rightpt] > k:
                rightpt -= 1
            else:
                leftpt += 1
                rightpt -= 1
                ans += 1
        return ans
                