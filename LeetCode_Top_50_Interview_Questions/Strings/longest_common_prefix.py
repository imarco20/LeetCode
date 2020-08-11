"""
9. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs: return ''
        m, M, i = min(strs), max(strs), 0
        for i in range(min(len(m),len(M))):
            if m[i] != M[i]: break
        else: i += 1
        return m[:i]
