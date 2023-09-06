from typing import Optional, List

from linked_list.ListNode import ListNode


# O(n) time || O(n) space
def split_list_to_parts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    cnt, curr = 0, head
    while curr:
        cnt, curr = cnt + 1, curr.next

    res = []
    res_len, ext = divmod(cnt, k)
    curr = head
    for _ in range(k):
        sentinel = ListNode()
        prev = sentinel

        for _ in range(res_len + (ext > 0)):
            sentinel.next, curr, sentinel = curr, curr.next, curr

        if ext > 0:
            ext -= 1

        sentinel.next = None
        res.append(prev.next)

    return res
