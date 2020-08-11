"""
3. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
"""

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        q = [root,root]

        while q:
            t1 = q.pop(0)
            t2 = q.pop(0)

            if not t1 and not t2:
                continue

            if t1 is None or t2 is None:
                return False

            if t1.val != t2.val:
                return False


            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)

        return True
