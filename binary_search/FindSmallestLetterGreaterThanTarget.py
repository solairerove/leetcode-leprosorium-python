from typing import List


# O(n) time || O(1) space
def next_greatest_letter_linear(self, letters: List[str], target: str) -> str:
    for char in letters:
        if char > target:
            return char

    return letters[0]
