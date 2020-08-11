"""
2. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        diff = 0
        ans = 0

        for i in range(len(prices)):

            if not stack:
                stack.append(prices[i])
            elif prices[i] < stack[-1]:
                stack.append(prices[i])

            if prices[i] > stack[-1]:
                diff = prices[i] - stack[-1]

            ans = max(ans, diff)

        return ans
