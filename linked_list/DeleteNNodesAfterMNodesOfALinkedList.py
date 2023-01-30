from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def delete_nodes(self, head: ListNode, m: int, n: int) -> ListNode:
    prev, curr = None, head
    while curr:
        skip = m
        while curr and skip > 0:
            skip, prev, curr = skip - 1, curr, curr.next

        remove = n
        while curr and remove > 0:
            remove, curr = remove - 1, curr.next

        prev.next = curr

    return head
