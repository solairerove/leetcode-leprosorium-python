from typing import List


# O(n * log(n)) time || O(1) space
def num_rescue_boats_naive(self, people: List[int], limit: int) -> int:
    if len(people) == 2 and sum(people) <= limit:
        return 1

    people.sort()

    res = 0
    low, high = 0, len(people) - 1
    while low <= high:
        hold = limit - people[high]
        if hold == 0:
            res += 1
            high -= 1
        elif people[low] - hold <= 0:
            res += 1
            low += 1
            high -= 1
        else:
            high -= 1
            res += 1

    return res
