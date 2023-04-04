from typing import List


# O(n) time || O(1) space
def maximum_even_split(self, final_sum: int) -> List[int]:
    res = []
    if final_sum % 2 != 0:
        return res

    i = 2
    while i <= final_sum:
        res.append(i)
        final_sum -= i
        i += 2
    res[-1] += final_sum

    return res
