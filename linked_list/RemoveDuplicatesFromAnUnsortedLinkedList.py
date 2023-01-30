from linked_list.ListNode import ListNode


# O(n) time || O(n) space
def delete_duplicates_unsorted(self, head: ListNode) -> ListNode:
    prev = sentinel = ListNode()
    curr = sentinel.next = head
    counter = dict()
    while curr:
        counter[curr.val] = counter.get(curr.val, 0) + 1
        curr = curr.next

    curr = head
    while curr:
        if counter[curr.val] > 1:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return sentinel.next
