class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        slowpt, fastpt = 0, 0
        ans = []
        while slowpt < len(nums) and fastpt < len(nums):
            if fastpt + 1 < len(nums) and nums[fastpt] + 1 == nums[fastpt + 1]:
                fastpt += 1
            else:
                if nums[slowpt] == nums[fastpt]:
                    ans.append(str(nums[slowpt]))
                    slowpt, fastpt =  slowpt + 1,fastpt + 1
                else:
                    ans.append(str(nums[slowpt]) + "->" + str(nums[fastpt]))
                    fastpt += 1
                    slowpt = fastpt
        return ans
