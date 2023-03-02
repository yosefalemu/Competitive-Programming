class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        ans = []
        for c in set1:
            if c in set2:
                ans.append(c)
        return ans
                
                
                
            
        
    
        
        
    
                
                
            
        