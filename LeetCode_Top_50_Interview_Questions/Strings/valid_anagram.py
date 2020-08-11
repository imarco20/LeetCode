"""
4. Valid Anagram
https://leetcode.com/problems/valid-anagram/
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        chars = {}

        for c in s:
            if c not in chars:
                chars[c] = 0
            chars[c] += 1

        for c in t:

            if c not in chars or chars[c] == 0:
                return False

            if c in chars:
                chars[c] -=1

        return not sum(chars.values())
