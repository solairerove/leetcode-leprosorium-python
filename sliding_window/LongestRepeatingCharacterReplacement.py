import collections


# O(n) time | O(1) space
def character_replacement(self, s: str, k: int) -> int:
    freq, max_freq, res = collections.defaultdict(int), 0, 0
    low = 0
    for high in range(len(s)):
        freq[s[high]] += 1
        # the maximum frequency of any character in the current window.
        max_freq = max(max_freq, freq[s[high]])

        # If the number of other characters (i.e., window length - max_freq) is greater than k
        if (high - low + 1) - max_freq > k:
            freq[s[low]] -= 1
            low += 1

        res = max(res, high - low + 1)

    return res
