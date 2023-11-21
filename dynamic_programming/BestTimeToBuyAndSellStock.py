from typing import List


# O(n) time || O(1) space
def max_profit(self, prices: List[int]) -> int:
    min_price, res = prices[0], 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            res = max(res, price - min_price)

    return res
