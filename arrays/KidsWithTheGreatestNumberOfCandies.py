from typing import List


# O(n) time || O(1) space
def kids_with_candies(self, candies: List[int], extra_candies: int) -> List[bool]:
    max_candies = max(candies)

    return [candy + extra_candies >= max_candies for candy in candies]
