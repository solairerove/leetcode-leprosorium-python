import collections
import heapq
from typing import List


# O(n) time || O(n) space
def top_k_frequent_quickselect(self, nums: List[int], k: int) -> List[int]:
    pairs = list(collections.Counter(nums).items())  # [(num, freq)]
    quickselect(pairs, 0, len(pairs) - 1, k)

    return [pair[0] for pair in pairs[:k]]


def quickselect(arr, low, high, k):
    if low == high:
        return

    i = partition(arr, low, high)
    if i == k:
        return
    elif i < k:
        quickselect(arr, i + 1, high, k)
    else:
        quickselect(arr, low, i - 1, k)


def partition(arr, low, high):
    pivot = arr[high][1]
    i = low
    for j in range(low, high):
        if arr[j][1] > pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]

    return i


# O(n) time || O(n) space
def top_k_frequent_linear(self, nums: List[int], k: int) -> List[int]:
    cnt = collections.Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in cnt.items():
        buckets[freq].append(num)

    res = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            res.append(num)

            if len(res) == k:
                return res


# O(n * log(k)) time || O(n + k) space
def top_k_frequent_heap(self, nums: List[int], k: int) -> List[int]:
    cnt = collections.Counter(nums)

    return heapq.nlargest(k, cnt.keys(), key=cnt.get)
