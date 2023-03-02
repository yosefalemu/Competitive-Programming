class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        temp = set(nums)
        ans = []
        for c in temp:
            ans.append(c)
        ans.sort(reverse = True)
        n = len(ans)
        if n >= 3:
            return ans[2]
        else:
            return ans[0]
            
        