from linked_list.ListNode import ListNode


# O(1) time || O(1) space
def delete_node(self, node: ListNode):
    node.val = node.next.val
    node.next = node.next.next
