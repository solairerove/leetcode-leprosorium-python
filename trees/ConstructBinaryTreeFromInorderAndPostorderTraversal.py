from typing import List, Optional

from trees.TreeNode import TreeNode


# O(n) time || O(n) space
def build_tree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    def build(left_idx, right_idx):
        if left_idx > right_idx:
            return None

        val = postorder.pop()
        root = TreeNode(val)

        idx = idx_map[val]
        root.right, root.left = build(idx + 1, right_idx), build(left_idx, idx - 1)

        return root

    idx_map = {val: idx for idx, val in enumerate(inorder)}

    return build(0, len(inorder) - 1)
