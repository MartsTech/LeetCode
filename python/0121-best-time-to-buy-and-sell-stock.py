class Solution:
    # O(n) time | O(1) space
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_price = float("-inf")
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
                max_price = price
            if price > max_price:
                max_price = price
                profit = max_price - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit