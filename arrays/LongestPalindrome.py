import collections


# O(n) time | O(1) space
def longest_palindrome(self, s: str) -> int:
    odds = sum(v % 2 for v in collections.Counter(s).values())

    return len(s) - odds + bool(odds)
