"""
11. Rotate Image
https://leetcode.com/problems/rotate-image/
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) # Number of Rows
        m = len(matrix[0]) # Number of Columns

        for i in range(n//2):
            matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]

        level = 0
        for i in range(n):
            for j in range(m):
                if i >= level and j >= level and i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            level += 1
