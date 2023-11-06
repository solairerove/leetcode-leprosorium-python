from typing import List


# O(n) time || O(1) space
def partition_labels(self, s: str) -> List[int]:
    last_occurrence = {c: i for i, c in enumerate(s)}
    res = []
    low = high = 0
    for i, c in enumerate(s):
        high = max(high, last_occurrence[c])

        if i == high:
            res.append(high - low + 1)
            low = high + 1

    return res
