from typing import Optional

from linked_list.ListNode import ListNode
from trees.TreeNode import TreeNode


# O(max(n * log(n), n^2)) time || O((log(n), n)) space
def sorted_list_to_bst(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    if not head:
        return

    if not head.next:
        return TreeNode(head.val)

    prev, slow, fast = None, head, head
    while fast and fast.next:
        prev, slow, fast = slow, slow.next, fast.next.next
    prev.next = None

    root = TreeNode(slow.val)
    root.left = sorted_list_to_bst(self, head)
    root.right = sorted_list_to_bst(self, slow.next)

    return root
