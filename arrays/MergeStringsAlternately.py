from itertools import zip_longest


# O(n + m) time || O(n + m) space
def merge_alternately(self, word1: str, word2: str) -> str:
    idx1, idx2, res = 0, 0, ""
    while idx1 < len(word1) and idx2 < len(word2):
        if idx1 <= idx2:
            res += word1[idx1]
            idx1 += 1
        else:
            res += word2[idx2]
            idx2 += 1

    if idx1 < len(word1):
        res += word1[idx1:]
    elif idx2 < len(word2):
        res += word2[idx2:]

    return res


# O(n + m) time || O(n + m) space
def merge_alternately_one_liner(self, word1: str, word2: str) -> str:
    return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
