import bisect
from typing import List

# classic binary search

# O(log(n)) time || O(1) space
def next_greatest_letter(self, letters: List[str], target: str) -> str:
    idx = bisect.bisect(letters, target)

    return letters[idx % len(letters)]


# O(n) time || O(1) space
def next_greatest_letter_linear(self, letters: List[str], target: str) -> str:
    for char in letters:
        if char > target:
            return char

    return letters[0]
