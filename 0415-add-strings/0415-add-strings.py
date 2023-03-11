class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        ans = ""
        while i >= 0 or j >= 0:
            if i >= 0  and j >= 0:
                sum = int(num1[i]) + int(num2[j]) + carry
            elif i >= 0:
                sum = int(num1[i]) + carry
            else:
                sum = int(num2[j]) + carry
            carry = sum // 10
            sum = sum % 10
            ans = str(sum) + ans
            i -= 1
            j -= 1
        if carry:
            return str(carry) + ans
        else:
            return ans
                
                
        