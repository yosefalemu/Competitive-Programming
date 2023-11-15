class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            for n in str(i):
                if(n == "0" or i % int(n) != 0):
                    break
            else:
                ans.append(int(i))
        return ans
                
                    
            
        
        
