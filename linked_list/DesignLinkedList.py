class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.nxt = None


class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.size = 0

        self.head.nxt = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index > self.size:
            return -1

        curr, res, i = self.head, None, 0
        if self.size - index > self.size // 2:
            while curr and i < index:
                curr = curr.nxt
                i += 1
            res = curr.nxt
        else:
            curr = self.tail
            while curr and i < self.size - index:
                curr = curr.prev
                i += 1
            res = curr.prev

        return res.val if res else -1

    def add_at_head(self, val: int) -> None:
        node = Node(val)
        head, nxt = self.head, self.head.nxt

        node.prev, node.nxt = head, nxt
        head.nxt = nxt.prev = node

        self.size += 1

    def add_at_tail(self, val: int) -> None:
        node = Node(val)
        tail, prev = self.tail, self.tail.prev

        node.prev, node.nxt = prev, tail
        tail.prev = prev.nxt = node

        self.size += 1

    def add_at_index(self, index: int, val: int) -> None:
        if index > self.size:
            return None

        node = Node(val)
        curr, i = self.head, 0
        if self.size - index > self.size // 2:
            while curr and i < index:
                curr = curr.nxt
                i += 1
            nxt = curr.nxt
            node.prev, node.nxt = curr, nxt
            curr.nxt, nxt.prev = node

        else:
            curr = self.tail
            while curr and i < self.size - index:
                curr = curr.prev
                i += 1
            prev = curr.prev
            node.prev, node.nxt = prev, curr
            prev.nxt = curr.prev = node

        self.size += 1

    def delete_at_index(self, index: int) -> None:
        if index > self.size:
            return None

        curr, i = self.head, 0
        if self.size - index > self.size // 2:
            while curr and i < index:
                curr = curr.nxt
                i += 1
            prev, nxt = curr, curr.nxt.nxt
            prev.nxt = nxt
            nxt.prev = prev

        else:
            curr = self.tail
            while curr and i < self.size - index:
                curr = curr.prev
                i += 1
            prev, nxt = curr.prev.prev, curr
            prev.nxt = nxt
            nxt.prev = prev

        self.size -= 1
