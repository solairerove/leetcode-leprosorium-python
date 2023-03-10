from functools import lru_cache


# O(n) time || O(1) space
def num_decodings(self, s: str) -> int:
    if s[0] == "0":
        return 0

    one_back = two_back = 1
    for i in range(1, len(s)):
        curr = 0
        if s[i] != "0":
            curr = one_back

        two_digit = int(s[i - 1: i + 1])
        if 10 <= two_digit <= 26:
            curr += two_back
        two_back, one_back = one_back, curr

    return one_back


# O(n) time || O(n) space
def num_decodings_recursive(self, s: str) -> int:
    @lru_cache(maxsize=None)
    def helper(ith: int) -> int:
        if ith == len(s):
            return 1

        if s[ith] == "0":
            return 0

        if ith == len(s) - 1:
            return 1

        res = helper(ith + 1)
        if 9 < int(s[ith: ith + 2]) < 27:
            res += helper(ith + 2)

        return res

    return helper(0)


# O(n) time || O(1) space
def num_decodings_this_is_python(self, s: str) -> int:
    prev_ways, curr_ways, prev_digit = 0, 1, ''
    for curr_digit in s:
        tmp = curr_ways
        curr_ways = (curr_digit > '0') * curr_ways + (10 <= int(prev_digit + curr_digit) <= 26) * prev_ways
        prev_ways, prev_digit = tmp, curr_digit

    return curr_ways
