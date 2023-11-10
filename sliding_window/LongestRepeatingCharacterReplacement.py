# O(n) time | O(1) space
import collections


def character_replacement(self, s: str, k: int) -> int:
    freq, max_freq, res = collections.defaultdict(int), 0, 0
    low = 0
    for high in range(len(s)):
        freq[s[high]] += 1
        max_freq = max(max_freq, freq[s[high]])

        if (high - low + 1) - max_freq > k:
            freq[s[low]] -= 1
            low += 1

        res = max(res, high - low + 1)

    return res
