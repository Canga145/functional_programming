class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev = prices[0]

        for price in prices[1:]:
            profit += (price - prev) if price > prev else 0
            prev = price

        return profit
