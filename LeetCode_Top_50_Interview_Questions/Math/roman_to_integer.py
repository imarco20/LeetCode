"""
4. Roman to Integer
https://leetcode.com/problems/roman-to-integer/
"""

class Solution:
    def romanToInt(self, s: str) -> int:

        romans = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D': 500, 'M' : 1000}
        irreg = {'I' : ('V', 'X'), 'X' : ('L', 'C'), 'C' : ('D', 'M')}


        total = 0
        i = 0

        while i < len(s) - 1:

            print(total, i)
            if s[i] in irreg and s[i+1] in irreg[s[i]]:
                total += (romans[s[i+1]] - romans[s[i]])
                i += 1

            else:
                total += romans[s[i]]

            i += 1

        if i < len(s):
            total += romans[s[-1]]

        return total
