class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ""
        i = 0
        j = 0
        a = a[::-1]
        b = b[::-1]
        while i < len(a) or j < len(b):
            if i < len(a) and j < len(b):
                digitA = int(a[i])
                digitB = int(b[j])
            elif i < len(a) and j >= len(b):
                digitA = int(a[i])
                digitB = 0
            elif i >= len(a) and j < len(b):
                digitA = 0
                digitB = int(b[j])
            else:
                pass
            i += 1
            j += 1
            total = digitA + digitB + carry
            sum1 = total % 2
            carry = total // 2
            ans += str(sum1)
        if carry:
            return "1" + ans[::-1]
        else:
            return ans[::-1]
            
            
            
        
                
            
        