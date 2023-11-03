import collections
import heapq
from typing import List


# O(n + m * log(m)) time || O(m) space
# n is number of words in list
# m is number of unique words
# k is number of top freq words
def top_k_frequent_sorting(self, words: List[str], k: int) -> List[str]:
    cnt = collections.Counter(words)

    return sorted(cnt, key=lambda word: (-cnt[word], word))[:k]


# O(n + k * log(m)) time || O(m) space
# n is number of words in list
# m is number of unique words
# k is number of top freq words
def top_k_frequent_heap(self, words: List[str], k: int) -> List[str]:
    heap = [(-freq, word) for word, freq in collections.Counter(words).items()]
    heapq.heapify(heap)

    return [heapq.heappop(heap)[1] for _ in range(k)]
