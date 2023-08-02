from typing import List


# O(n^2 * n!) time || O(n^2) space
def permute(self, nums: List[int]) -> List[List[int]]:
    res = []

    def dfs(arr, path):
        if not arr:
            res.append(path)
            return

        for i in range(len(arr)):
            dfs(arr[:i] + arr[i + 1:], path + [arr[i]])

    dfs(nums, [])

    return res
