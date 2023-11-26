class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if abs(target - (nums[i] + nums[left] + nums[right])) < diff:
                    diff = abs(target - (nums[i] + nums[left] + nums[right]))
                    ans = nums[i] + nums[left] + nums[right]
                if nums[i] + nums[left] + nums[right] < target:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > target:
                    right -= 1
                else:
                    return target
        return ans
        
