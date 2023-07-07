class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        ans = 0
        leftpt = rightpt = 0
        players.sort()
        trainers.sort()
        while leftpt < len(players) and rightpt < len(trainers):
            if players[leftpt] <= trainers[rightpt]:
                ans += 1
                leftpt += 1
            rightpt += 1
        return ans
        