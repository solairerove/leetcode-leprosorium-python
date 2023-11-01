import collections
import heapq
from typing import List


# O(n) time || O(n) space
def top_k_frequent_quickselect(self, nums: List[int], k: int) -> List[int]:
    if len(nums) == k:
        return nums

    cnt = collections.Counter(nums)
    unique = list(cnt.items())  # (number, frequency) pairs list

    kth_freq = quickselect(self, unique, 0, len(unique) - 1, k - 1)[1]  # kth pair

    return [item[0] for item in unique if item[1] >= kth_freq]


def quickselect(self, arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_idx = partition(self, arr, low, high)
    if k == pivot_idx:
        return arr[k]
    elif k < pivot_idx:
        return quickselect(self, arr, low, pivot_idx - 1, k)
    else:
        return quickselect(self, arr, pivot_idx + 1, high, k)


def partition(self, arr, low, high):
    pivot = arr[high][1]
    i = low
    for j in range(low, high):
        if arr[j][1] > pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]

    return i


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
