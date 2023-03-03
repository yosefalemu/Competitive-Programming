class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        time = 0
        for i in range(len(timeSeries)):
            if i + 1 < len(timeSeries) and timeSeries[i] + duration <= timeSeries[i + 1]:
                time += duration
            elif i + 1 == len(timeSeries):
                time += duration
            else:
                time += (timeSeries[i + 1] - timeSeries[i])
        return time
                
                
        