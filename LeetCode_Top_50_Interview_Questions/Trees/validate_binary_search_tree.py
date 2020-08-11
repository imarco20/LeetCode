"""
2. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
"""

class Solution:
    def inorder(self, root):

        if not root:
            return []

        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def isValidBST(self, root: TreeNode) -> bool:

        lst = self.inorder(root)

        for i in range(1, len(lst)):

            if lst[i] <= lst[i - 1]:
                return False

        return True
