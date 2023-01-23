from typing import Optional


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

    def get_prev_node_to(self, index: int) -> Optional[Node]:
        if index > self.size:
            return None

        # head -> 1 -> 2 -> 3 -> 4 -> 5 -> tail
        curr, res, i = self.head, None, 0
        if self.size - index >= self.size // 2:
            while curr and i < index:
                curr = curr.nxt
                i += 1
            res = curr
        else:
            curr = self.tail
            while curr and i < self.size - index:
                curr = curr.prev
                i += 1
            res = curr.prev.prev

        return res

    def get(self, index: int) -> int:
        if index > self.size:
            return -1

        return self.get_prev_node_to(index).nxt.val

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
        prev = self.get_prev_node_to(index)
        nxt = prev.nxt

        node.prev = prev
        node.nxt = nxt

        prev.nxt = node
        nxt.prev = node

        self.size += 1

    def delete_at_index(self, index: int) -> None:
        if index > self.size:
            return None

        prev = self.get_prev_node_to(index)
        nxt = prev.nxt.nxt

        prev.nxt = nxt
        nxt.prev = prev

        self.size -= 1
