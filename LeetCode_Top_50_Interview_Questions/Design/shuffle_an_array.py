"""
1. Shuffle An Array
https://leetcode.com/problems/shuffle-an-array/
"""

import copy
class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        lst = copy.deepcopy(self.array)
        n = len(lst)

        for i in range(n):
            idx = random.randint(0, n-1)
            lst[i], lst[idx] = lst[idx], lst[i]

        return lst
