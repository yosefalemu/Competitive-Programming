class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        totalSum = sum(skill)
        length = len(skill)
        numPair = length // 2
        desiredVal = totalSum // numPair
        skill.sort()
        chemistryTotal = 0
        leftpt = 0
        rightpt = length - 1
        while leftpt < rightpt:
            if skill[leftpt] + skill[rightpt] == desiredVal:
                chemistryTotal += skill[leftpt] * skill[rightpt]
            else:
                return -1
            leftpt += 1
            rightpt -= 1
        return chemistryTotal
        
        
        