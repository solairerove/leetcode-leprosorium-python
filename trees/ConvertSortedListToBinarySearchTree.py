from typing import Optional

from linked_list.ListNode import ListNode
from trees.TreeNode import TreeNode


# O(n) time || O(n) space
def sorted_list_to_bst_using_array(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    if not head:
        return

    if not head.next:
        return TreeNode(head.val)

    arr = linked_list_to_array(self, head)

    def convert_arr_to_bst(low, high):
        if high < low:
            return None

        mid = low + (high - low) // 2
        node = TreeNode(arr[mid])

        if low == high:
            return node

        node.left = convert_arr_to_bst(low, mid - 1)
        node.right = convert_arr_to_bst(mid + 1, high)

        return node

    return convert_arr_to_bst(0, len(arr) - 1)


def linked_list_to_array(self, head: Optional[ListNode]) -> []:
    arr = []
    while head:
        arr.append(head.val)
        head = head.next

    return arr


# O(max(n * log(n), n^2)) time || O((log(n), n)) space
def sorted_list_to_bst_rec(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    if not head:
        return

    if not head.next:
        return TreeNode(head.val)

    prev, slow, fast = None, head, head
    while fast and fast.next:
        prev, slow, fast = slow, slow.next, fast.next.next
    prev.next = None

    root = TreeNode(slow.val)
    root.left = sorted_list_to_bst_rec(self, head)
    root.right = sorted_list_to_bst_rec(self, slow.next)

    return root
