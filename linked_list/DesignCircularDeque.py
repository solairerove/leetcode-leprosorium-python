class Node:
    def __init__(self, value):
        self.val = value
        self.prev = self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = k
        self.size = 0

    def add_node(self, value: int, prev: Node):
        node = Node(value)
        node.prev = prev
        node.next = prev.next
        node.prev.next = node.next.prev = node
        self.size += 1

    def remove_node(self, prev: Node):
        node = prev.next
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def insert_front(self, value: int) -> bool:
        if not self.is_full():
            self.add_node(value, self.head)
            return True

        return False

    def insert_last(self, value: int) -> bool:
        if not self.is_full():
            self.add_node(value, self.tail.prev)
            return True

        return False

    def delete_front(self) -> bool:
        if not self.is_empty():
            self.remove_node(self.head)
            return True

        return False

    def delete_last(self) -> bool:
        if not self.is_empty():
            self.remove_node(self.tail.prev.prev)
            return True

        return False

    def get_front(self) -> int:
        if not self.is_empty():
            return self.head.next.val

        return -1

    def get_rear(self) -> int:
        if not self.is_empty():
            return self.tail.prev.val

        return -1

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity
