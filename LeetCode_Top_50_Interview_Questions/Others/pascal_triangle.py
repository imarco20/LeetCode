"""
4. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(0, numRows):
            ans = []
            for k in range(0,i+1):
                if i == 0 or k == 0:
                    ans.append(1)
                elif i == k:
                    ans.append(1)
                else:
                    a = result[i-1][k-1]
                    b = result[i-1][k]
                    ans.append(a + b)
            result.append(ans)
        return result
