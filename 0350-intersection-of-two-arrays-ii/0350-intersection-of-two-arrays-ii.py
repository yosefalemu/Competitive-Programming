class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        leftpt, rightpt = 0, 0
        while leftpt < len(nums1) and rightpt < len(nums2):
            if nums1[leftpt] == nums2[rightpt]:
                ans.append(nums1[leftpt])
                leftpt += 1
                rightpt += 1
            elif nums1[leftpt] < nums2[rightpt]:
                leftpt += 1
            else:
                rightpt += 1
    
        return ans
                
            
        
        