import collections


# O(n) time | O(1) space
def longest_palindrome(self, s: str) -> int:
    res = 0
    for v in collections.Counter(s).values():
        res += v // 2 * 2
        if res % 2 == 0 and v % 2 == 1:
            res += 1

    return res
