import collections
import heapq
from typing import List


class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, pair):
        return self.freq < pair.freq or (self.freq == pair.freq and self.word > pair.word)


# O(n * log(k)) time || O(n) space
# n is number of words in list
# k is number of top freq words
def top_k_frequent_min_heap(self, words: List[str], k: int) -> List[str]:
    cnt = collections.Counter(words)
    heap = []
    for word, freq in cnt.items():
        heapq.heappush(heap, Pair(word, freq))
        if len(heap) > k:
            heapq.heappop(heap)

    return [pair.word for pair in sorted(heap, reverse=True)]


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
    cnt = collections.Counter(words)
    heap = [(-freq, word) for word, freq in cnt.items()]
    heapq.heapify(heap)

    return [heapq.heappop(heap)[1] for _ in range(k)]


# O(n + m * log(m)) time || O(n + m) space
# n is number of words in list
# m is number of unique words
# k is number of top freq words
def top_k_frequent_bucket(self, words: List[str], k: int) -> List[str]:
    cnt = collections.Counter(words)

    buckets = collections.defaultdict(list)
    for word, freq in cnt.items():
        buckets[freq].append(word)

    for freq in buckets:
        buckets[freq].sort()

    res = []
    for freq in range(len(words), 0, -1):
        if freq in buckets:
            for word in buckets[freq]:
                res.append(word)
                if len(res) == k:
                    return res

    return res
