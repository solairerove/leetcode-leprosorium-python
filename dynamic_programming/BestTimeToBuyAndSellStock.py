from typing import List


# O(n) time || O(1) space
def max_profit(self, prices: List[int]) -> int:
    profit, min_price = 0, prices[0]
    for i in range(1, len(prices)):
        profit = max(profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])

    return profit
