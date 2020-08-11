"""
5. Single Number
https://leetcode.com/problems/single-number/
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        dicto = {}

        for num in nums:
            if num in dicto:
                del dicto[num]

            else:
                dicto[num] = 1

        for k, v in dicto.items():
            return k
