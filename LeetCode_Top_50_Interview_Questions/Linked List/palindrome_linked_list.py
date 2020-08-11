"""
4. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
"""

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        cur = head
        values = []

        while cur:
            values.append(cur.val)
            cur = cur.next

        n = len(values)

        i, j = 0, n - 1

        while i <= n//2 and j >= n//2:

            if values[i] != values[j]:
                return False

            i += 1
            j -= 1

        return True
