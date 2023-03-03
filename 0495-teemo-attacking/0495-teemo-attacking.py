class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        time = 0
        for i in range(len(timeSeries) - 1):
            if (timeSeries[i + 1] - timeSeries[i] < duration):
                time += (timeSeries[i + 1] - timeSeries[i])
            else:
                time += duration
        return time + duration
                
                
                
        