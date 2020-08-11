"""
2. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        i = head
        j = head
        count = 0

        while j and count < n:
            count += 1
            j = j.next

        if not j:
            return i.next

        while j:

            if not j.next:
                i.next = i.next.next
                break
            else:

                i = i.next
                j = j.next

        return head
