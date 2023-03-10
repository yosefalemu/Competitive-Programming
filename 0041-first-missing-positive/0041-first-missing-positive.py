class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        record={}
        
        for n in nums:
            if n in record or n<=0:
                continue
            record[n]=[1,1]           
            rightlength,leftlength=0,0
            
            if n-1 in record:
                leftlength=record[n-1][0] 
                record[n][0]+=leftlength
            if n+1 in record:
                rightlength=record[n+1][1]
                record[n][1]+=rightlength
                
            if n-1 in record:
                record[n-leftlength][1]+=record[n][1]
            if n+1 in record:
                record[n+rightlength][0]+=record[n][0]
                 
        return record[1][1]+1 if 1 in record else 1
        