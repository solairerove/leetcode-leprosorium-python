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
# insert at high and change // with %
        if cnt > 1:
            position_to_insert = 1
            while cnt >= 10:
                chars.insert(low + position_to_insert, str(cnt // 10))
                cnt %= 10
                position_to_insert += 1

            chars.insert(low + position_to_insert, str(cnt))
            low, high = low + 1, high + 1

        low, high = low + 1, high + 1

    return len(chars)
