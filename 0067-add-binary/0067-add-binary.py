class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = []
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 :
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            temp = total % 2
            carry = total // 2
            ans.append(str(temp))
        if carry:
            return "1" + "".join(reversed(ans))
        else:
            return "".join(reversed(ans))
                
            
            
            
        
                
            
        