"""
3. Reverse Bits
https://leetcode.com/problems/reverse-bits/
"""

class Solution:
    def reverseBits(self, n: int) -> int:

        ans, i = 0, 31

        while n:

            ans += (n & 1) << i
            n = n >> 1
            i -= 1

        return ans
