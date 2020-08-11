"""
1. Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/
"""

class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0

        while n:

            if n & 1:
                count +=1

            n >>= 1

        return count
