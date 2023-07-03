class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        leftpt = 0
        rightpt = len(people) - 1
        people.sort()
        while leftpt <= rightpt:
            if people[rightpt] + people[leftpt] <= limit:
                leftpt += 1
                rightpt -= 1
            else:
                rightpt -= 1
            ans += 1
        return ans
            
        