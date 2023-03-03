class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        index = 0
        ans = [-1] *(len(nums1))
        for c in nums2:
            dict1.update({c:index})
            index += 1
        for i in range(len(nums1)):
            for j in range(dict1[nums1[i]], len(nums2)):
                if nums1[i] < nums2[j]:
                    ans[i] = nums2[j]
                    break
        return ans
                
        