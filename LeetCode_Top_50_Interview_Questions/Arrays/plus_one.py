"""
7. Plus One
https://leetcode.com/problems/plus-one/
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        j = len(digits) - 1

        while  j >= 0:

            if digits[j] == 9:
                if j > 0:
                    digits[j] = 0
                if j == 0:
                    digits.insert(0, 1)
                    digits[1] = 0
            else:
                digits[j] += 1
                break

            j -= 1

        return digits
