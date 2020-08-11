"""
2. First Bad Version
https://leetcode.com/problems/first-bad-version/
"""

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left, right = 1, n

        while left <= right:

            mid = left + (right - left) // 2

            if isBadVersion(mid):
                if mid == 1:
                    return mid

                right = mid - 1

            elif (isBadVersion(mid) != True and isBadVersion(mid+1) == True):
                return mid + 1

            else:
                left = mid + 1
