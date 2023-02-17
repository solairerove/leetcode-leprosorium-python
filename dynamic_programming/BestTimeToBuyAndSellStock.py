from typing import List


# O(n) time || O(1) space
def max_profit(self, prices: List[int]) -> int:
    profit = 0
    curr_min = prices[0]
    for i in range(1, len(prices)):
        price = prices[i]

        profit = max(profit, price - curr_min)
        curr_min = min(curr_min, price)

    return profit
