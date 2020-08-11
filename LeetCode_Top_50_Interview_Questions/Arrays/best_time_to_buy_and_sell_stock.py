"""
2. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""
class Solution:
  def maxProfit(self, prices: List[int]) -> int:

      profit = 0
      peak = prices[0]
      valley = prices[0]
      i = 0
      while i < len(prices) - 1:

          while i < len(prices) - 1 and prices[i] >= prices[i+1]:
              i += 1
          valley = prices[i]

          while i < len(prices) - 1 and prices[i] <= prices[i+1]:
              i += 1
          peak = prices[i]

          profit += (peak - valley)

      return profit
