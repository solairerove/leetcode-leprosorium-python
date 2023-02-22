from typing import List


# O(n * log(n)) time || O(1) space
def ship_within_days(self, weights: List[int], days: int) -> int:
    low, high = max(weights), sum(weights)
    while low <= high:
        mid, need, curr = low + (high - low) // 2, 1, 0

        for w in weights:
            if curr + w > mid:
                need += 1
                curr = 0
            curr += w

        if need > days:
            low = mid + 1
        else:
            high = mid - 1

    return low
