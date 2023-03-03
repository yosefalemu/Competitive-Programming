class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count = 0
        for i in range(len(timeSeries)):
            if i + 1 < len(timeSeries) and timeSeries[i] + duration <= timeSeries[i + 1]:
                count += duration
            elif i + 1 == len(timeSeries):
                count += duration
            else:
                count += (timeSeries[i + 1] - timeSeries[i])
        return count
                
                
        