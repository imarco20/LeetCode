"""
6. Missing Number
https://leetcode.com/problems/missing-number/
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        total = (n)*(n+1)//2

        for i in range(len(nums)):

            total -= nums[i]

        return total
