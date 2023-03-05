import collections
from typing import List


# O(n) time || O(n) space
def min_jumps(self, arr: List[int]) -> int:
    if len(arr) == 1:
        return 0

    el_to_idx = collections.defaultdict(list)
    for i, n in enumerate(arr):
        el_to_idx[n].append(i)

    dp = [0] * len(arr)
    dq = collections.deque([len(arr) - 1])
    while dq:
        i = dq.popleft()

        if i < len(arr) - 2 and dp[i + 1] == 0:
            dp[i + 1] = dp[i] + 1
            dq.append(i + 1)

        if i > 0 and dp[i - 1] == 0:
            dp[i - 1] = dp[i] + 1
            if i - 1 == 0:
                return dp[0]

            dq.append(i - 1)

        for j in el_to_idx[arr[i]]:
            if dp[j] == 0 and j < len(arr) - 1:
                dp[j] = dp[i] + 1
                if j == 0:
                    return dp[0]

                dq.append(j)

        el_to_idx.pop(arr[i])

    return dp[0]
