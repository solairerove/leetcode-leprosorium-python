from typing import Optional


class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev, self.nxt = None, None


class MyLinkedList:

    def __init__(self):
        self.head, self.tail = Node(-1), Node(-1)
        self.size = 0

        self.head.nxt, self.tail.prev = self.tail, self.head

    def get_prev_node_to(self, index: int) -> Optional[Node]:
        if index > self.size:
            return None

        if self.size - index >= self.size // 2:
            curr = self.head
            for i in range(index):
                curr = curr.nxt
        else:
            curr = self.tail
            for i in range(self.size - index):
                curr = curr.prev
            curr = curr.prev

        return curr

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

        if index == self.size:
            self.add_at_tail(val)
            return None
        elif index == 0:
            self.add_at_head(val)
            return None

        node = Node(val)
        prev = self.get_prev_node_to(index)
        nxt = prev.nxt

        node.prev, node.nxt = prev, nxt
        prev.nxt = nxt.prev = node

        self.size += 1

    def delete_at_index(self, index: int) -> None:
        if index >= self.size:
            return None

        prev = self.get_prev_node_to(index)
        nxt = prev.nxt.nxt

        prev.nxt = nxt
        nxt.prev = prev

        self.size -= 1
