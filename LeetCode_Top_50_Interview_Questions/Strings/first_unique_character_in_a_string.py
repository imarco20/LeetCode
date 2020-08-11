"""
3. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}

        for c in s:
            if c not in chars:
                chars[c] = 0
            chars[c] += 1

        for i in range(len(s)):
            if chars[s[i]] == 1:
                return i

        return -1
