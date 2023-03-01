class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        i = 10**(len(num1) - 1)
        j = 10**(len(num2) - 1)
        ans1, ans2 = 0, 0 
        for c in num1:
            ans1 += num[c]*i
            i //= 10
        for c in num2:
            ans2 += num[c]*j
            j //= 10
        return str(ans1*ans2)
