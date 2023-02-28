import collections
from typing import Optional, List

from trees.TreeNode import TreeNode


# O(n) time || O(n) space
def find_duplicate_subtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    nodes = collections.defaultdict(list)

    def traverse(node):
        if not node:
            return "null"

        key = "%s,%s,%s" % (str(node.val), traverse(node.left), traverse(node.right))
        nodes[key].append(node)

        return key

    traverse(root)

    return [nodes[key][0] for key in nodes if len(nodes[key]) > 1]
