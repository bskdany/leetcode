class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      l = 0
      min_val = prices[l]
      max_profit = 0
      for r in range(1, len(prices)):
        max_profit = max(max_profit, prices[r] - min_val)

        if prices[r] < min_val:
          min_val = prices[r]
          l = r
      return max_profit

        