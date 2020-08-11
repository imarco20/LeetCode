"""
5. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""

        for c in s:
            if c.isalnum():
                a += c.lower()

        i, j = 0, len(a) - 1

        while i < j:

            if a[i] != a[j]:
                return False
            i += 1
            j -= 1

        return True
