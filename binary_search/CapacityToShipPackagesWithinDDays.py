from typing import List


# O(n * log(n)) time || O(1) space
def ship_within_days(self, weights: List[int], days: int) -> int:
    low, high = max(weights), sum(weights)
    while low <= high:
        mid = low + (high - low) // 2
        days_required, curr_weight = 1, 0
        for weight in weights:
            if curr_weight + weight <= mid:
                curr_weight += weight
            else:
                days_required, curr_weight = days_required + 1, weight

        if days_required <= days:
            high = mid - 1
        else:
            low = mid + 1

    return low
