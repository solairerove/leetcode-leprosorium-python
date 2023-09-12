import collections


# O(n) time || O(1) space
def min_deletions(self, s: str) -> int:
    cnt, res, used = collections.Counter(s), 0, set()
    for ch, freq in cnt.items():
        while freq > 0 and freq in used:
            freq, res = freq - 1, res + 1
        used.add(freq)

    return res
