from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(n) space
def is_balanced_rec(self, root: Optional[TreeNode]) -> bool:
    def dfs(node):
        if not node:
            return 0, True

        l_height, l_balanced = dfs(node.left)
        r_height, r_balanced = dfs(node.right)

        return max(l_height, r_height) + 1, l_balanced and r_balanced and abs(l_height - r_height) <= 1

    return dfs(root)[1]


# O(n) time || O(n) space
def is_balanced_dfs(self, root: Optional[TreeNode]) -> bool:
    stack = [(root, 0, False)]
    heights = {}
    while stack:
        node, height, visited = stack.pop()

        if not node:
            continue

        if visited:
            l_height = heights.get(node.left, 0)
            r_height = heights.get(node.right, 0)

            if abs(l_height - r_height) > 1:
                return False

            heights[node] = 1 + max(l_height, r_height)
        else:
            stack.append((node, height, True))
            stack.append((node.left, height + 1, False))
            stack.append((node.right, height + 1, False))

    return True
