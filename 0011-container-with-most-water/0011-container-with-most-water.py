class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftpt = 0
        rightpt = len(height) - 1
        ans = 0
        while leftpt < rightpt:
            currentArea = min(height[leftpt],height[rightpt]) * (rightpt - leftpt)
            ans = max(ans, currentArea)
            if height[leftpt] <= height[rightpt]:
                leftpt += 1
            else:
                rightpt -= 1
        return ans
        