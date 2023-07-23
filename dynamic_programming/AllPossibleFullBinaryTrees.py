from typing import List, Optional

from dynamic_programming.HouseRobberIII import TreeNode


# O(2 ^ n) time || O(2 ^ n) space
def all_possible_fbt(self, n: int) -> List[Optional[TreeNode]]:
    mem = {1: [TreeNode(0)]}

    def dp(N):
        if N % 2 == 0:
            return []

        if N not in mem:
            res = []
            for i in range(1, N, 2):
                for left in dp(i):
                    for right in dp(N - 1 - i):
                        root = TreeNode(0)
                        root.left, root.right = left, right

                        res.append(root)
            mem[N] = res

        return mem[N]

    return dp(n)
