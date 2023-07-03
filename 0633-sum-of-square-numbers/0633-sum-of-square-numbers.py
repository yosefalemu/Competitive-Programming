class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        leftpt = 0
        rightpt = int(c**0.5)
        while leftpt <= rightpt:
            currSum = leftpt**2 + rightpt**2 
            if currSum == c:
                return True
            elif currSum < c:
                leftpt += 1
            else:
                rightpt -= 1
        return False
                
                
        