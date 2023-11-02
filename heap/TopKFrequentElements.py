import collections
import heapq
from typing import List


# O(n) time || O(n) space
def top_k_frequent_quickselect(self, nums: List[int], k: int) -> List[int]:
    def partition(arr, low, high):
        pivot = arr[high][1]
        i = low
        for j in range(low, high):
            if arr[j][1] > pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[high] = arr[high], arr[i]

        return i

    def quickselect(arr, low, high):
        if low == high:
            return

        i = partition(arr, low, high)
        if i == k:
            return
        elif i < k:
            quickselect(arr, i + 1, high)
        else:
            quickselect(arr, low, i - 1)

    pairs = list(collections.Counter(nums).items())  # [(key, freq)]
    quickselect(pairs, 0, len(pairs) - 1)

    return [pair[0] for pair in pairs[:k]]


# O(n) time || O(n) space
def top_k_frequent_linear(self, nums: List[int], k: int) -> List[int]:
    if len(nums) == k:
        return nums

    cnt = collections.Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in cnt.items():
        buckets[freq].append(num)

    res = []
    for i in range(len(nums), 0, -1):
        for num in buckets[i]:
            res.append(num)

            if len(res) == k:
                return res


# O(n * log(k)) time || O(n + k) space
def top_k_frequent_heap(self, nums: List[int], k: int) -> List[int]:
    if len(nums) == k:
        return nums

    cnt = collections.Counter(nums)

    return heapq.nlargest(k, cnt.keys(), key=cnt.get)
