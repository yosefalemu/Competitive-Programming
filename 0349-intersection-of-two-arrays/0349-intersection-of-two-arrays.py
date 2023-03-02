class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        temp = []
        for c in nums1:
            if c in dict1:
                pass
            else:
                dict1[c] = 1
        for c in nums2:
            if c in dict1:
                temp.append(c)
        return list(set(temp))
            
        
    
                
                
            
        