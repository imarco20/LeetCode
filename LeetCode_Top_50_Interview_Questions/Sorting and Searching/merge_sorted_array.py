"""
1. Merge Sorted Array

"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) > 1:
            i = j = 0
            for k in range(len(nums1)):
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    nums1.insert(k,nums2[j])
                    nums1.pop(-1)
                    j += 1
            print (j)
            if j < len(nums2):
                for __ in range(len(nums2)-j):
                    nums1.pop(-1)
                nums1.extend(nums2[j:])
