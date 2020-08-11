"""
4. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return root
        queue = []
        return_list = []
        queue.append(root)
        while len(queue) > 0:
            ans = []
            # print(ans)
            l = len(queue)
            for l in range(l):
                node = queue.pop(0)
                ans.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                print(ans)
            return_list.append(ans)
        return return_list
