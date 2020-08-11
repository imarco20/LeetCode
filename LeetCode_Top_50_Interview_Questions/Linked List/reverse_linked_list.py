"""
6. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        previous = None
        current = head
        nextnode = None

        while current:
            nextnode = current.next

            current.next = previous
            previous = current
            current = nextnode

        return previous
