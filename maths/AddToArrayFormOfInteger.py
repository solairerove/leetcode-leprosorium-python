from typing import List


# O(n) time || O(1) space
def add_to_array_form(self, num: List[int], k: int) -> List[int]:
    for i in range(len(num) - 1, -1, -1):
        k, num[i] = divmod(num[i] + k, 10)

    return [int(i) for i in str(k)] + num if k else num
