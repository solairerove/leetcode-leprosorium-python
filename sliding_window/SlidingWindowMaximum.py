import collections
from typing import List


# O(n) time | O(k) space
def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
    res = []
    dq = collections.deque()
    for i, n in enumerate(nums):
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and nums[dq[-1]] <= n:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            res.append(nums[dq[0]])

    return res
