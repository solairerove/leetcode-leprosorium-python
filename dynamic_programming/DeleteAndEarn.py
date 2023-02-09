from typing import List


# O(max(n)) time || O(max(n)) space
def delete_and_earn(self, nums: List[int]) -> int:
    if not nums:
        return 0

    freq = [0] * (max(nums) + 1)
    for n in nums:
        freq[n] += n

    dp = [0] * len(freq)
    dp[1] = 1
    for i in range(2, len(freq)):
        dp[i] = max(freq[i - 1], freq[i - 2] + freq[i])

    return dp[-1]
