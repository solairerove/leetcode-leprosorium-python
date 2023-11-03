import collections
from typing import List


# O(n + m * log(m)) time || O(m) space
# n is number of words in list
# m is number of unique words
def top_k_frequent_sorting(self, words: List[str], k: int) -> List[str]:
    cnt = collections.Counter(words)

    return sorted(cnt, key=lambda word: (-cnt[word], word))[:k]
