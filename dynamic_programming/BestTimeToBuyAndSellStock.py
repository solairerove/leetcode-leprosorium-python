from typing import List


# O(n) time || O(1) space
def max_profit(self, prices: List[int]) -> int:
    profit, min_price = 0, prices[0]
    for i in range(1, len(prices)):
        price = prices[i]

        profit = max(profit, price - min_price)
        min_price = min(min_price, price)

    return profit
