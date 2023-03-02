from typing import List


# O(n) time || O(1) space
def compress(self, chars: List[str]) -> int:
    if len(chars) == 1:
        return 1

    low, high = 0, 1
    while high < len(chars):
        cnt = 1
        while high < len(chars) and chars[low] == chars[high]:
            chars.pop(high)
            cnt += 1

        if cnt > 1:
            position_to_insert = 1
            for c in str(cnt):
                chars.insert(low + position_to_insert, c)
                position_to_insert += 1
                high = high + 1
            low = high - 1

        low, high = low + 1, high + 1

    return len(chars)
