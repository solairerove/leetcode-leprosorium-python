from typing import List


# O(n * log(n)) time || O(n) space
def num_rescue_boats(self, people: List[int], limit: int) -> int:
    people.sort()
    low, high = 0, len(people) - 1
    res = 0
    while low <= high:
        res += 1
        if people[low] + people[high] <= limit:
            low += 1

        high -= 1

    return res
