"""
5. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""

class Solution:

    def bst(self, nums):

        left, right = 0, len(nums) - 1

        if left > right:
            return

        mid = left + (right - left) // 2

        root = TreeNode(nums[mid])

        root.left = self.bst(nums[0:mid])
        root.right = self.bst(nums[mid+1:])

        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        return self.bst(nums)
