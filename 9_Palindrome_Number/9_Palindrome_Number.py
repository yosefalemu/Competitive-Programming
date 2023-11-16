class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        newNum = 0
        while temp > 0:
            newNum = (10*newNum + temp%10)
            temp = temp//10
        return x == newNum
