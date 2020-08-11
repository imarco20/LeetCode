"""
7. Implement strStr()
https://leetcode.com/problems/implement-strstr/

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0

        if len(needle) > len(haystack):
            return -1

        a = len(needle)

        for i in range(len(haystack)):
            if haystack[i:i+a] == needle:
                return i

        return -1
