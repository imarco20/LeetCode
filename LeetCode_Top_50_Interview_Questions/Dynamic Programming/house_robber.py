"""
4. House Robber
https://leetcode.com/problems/house-robber/
"""

class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        dp = [0]*len(nums)


        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max((nums[2] + nums[0]), nums[1])


        for i in range(3, len(nums)):

            dp[i] = max((nums[i] + dp[i-2]), (nums[i] + dp[i-3]), dp[i-1])

        return dp[-1]
