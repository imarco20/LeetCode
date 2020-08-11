"""
6. String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/
"""

class Solution:
    def myAtoi(self, str: str) -> int:

        if len(str) == 1 and str.isdigit(): return int(str)

        for i, c in enumerate(str):
            if c == ' ': continue
            if c in '+-' or c.isdigit(): break
            return 0

        if (len(str) <= 1 and not str.isdigit()) or (i == len(str)-1) or (str[i] in '+-' and not str[i+1].isdigit()): return 0

        for j in range(i+1,len(str)):
            if not str[j].isdigit(): break
        str = int(str[i:j+str[j].isdigit()])
        return min(str, 2**31 - 1) if str >= 0 else max(str, -(2**31))
