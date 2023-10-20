# O(log(n)) time || O(1) space
def guess_number(self, n: int, pick: int) -> int:
    low, high = 1, n
    while low <= high:
        mid = low + (high - low) // 2
        cmp = guess(self, mid, pick)
        if cmp == 0:
            return mid
        elif cmp == -1:
            high = mid - 1
        else:
            low = mid + 1


# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(self, num: int, pick: int) -> int:
    if pick < num:
        return -1
    elif pick > num:
        return 1

    return 0
