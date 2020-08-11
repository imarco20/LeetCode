"""
2. Hamming Distance
https://leetcode.com/problems/hamming-distance/
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return "{0:b}".format(x ^ y).count("1")
