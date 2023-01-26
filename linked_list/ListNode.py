class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class RandomListNode:
    def __init__(self, x: int, next: 'RandomListNode' = None, random: 'RandomListNode' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class ChildListNode:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
