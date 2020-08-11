"""
10. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/
"""

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.issquarevalid(board) and self.isrowvalid(board) and self.iscolvalid(board))

    def issquarevalid(self, board):
        for i in (0,3,6):
            for j in (0,3,6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]

                if not self.isunitvalid(square):
                    return False
        return True

    def isrowvalid(self, board):
        for row in board:
            if not self.isunitvalid(row):
                return False
        return True

    def iscolvalid(self, board):
        for col in zip(*board):
            if not self.isunitvalid(col):
                return False
        return True

    def isunitvalid(self, unit):

        unit = [i for i in unit if i != '.']

        return len(set(unit)) == len(unit)
