class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        n=len(nums1)
        for i in nums1:
            if i in nums2:
                ans.append(i)
        return list(set(ans))
        