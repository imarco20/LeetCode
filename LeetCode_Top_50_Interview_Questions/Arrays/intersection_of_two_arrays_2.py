"""
6. Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        intersection = []
        num1Dict = {}

        for n in nums1:
            num1Dict[n] = num1Dict[n] + 1 if n in num1Dict else 1

        for n in nums2:
            if n in num1Dict and num1Dict[n] > 0:
                intersection.append(n)
                num1Dict[n] = num1Dict[n] - 1

        return intersection
