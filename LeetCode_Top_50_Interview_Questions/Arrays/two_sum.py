"""
9. Two Sum
https://leetcode.com/problems/two-sum/
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicto = {}

        for i in range(len(nums)):
            dicto[target - nums[i]] = i

        for i, num in enumerate(nums):
            if num in dicto and dicto[num] != i:
                return [i, dicto[num]]
