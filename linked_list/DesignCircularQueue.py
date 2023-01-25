class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.head = self.tail = None
        self.capacity = k
        self.size = 0

    def en_queue(self, value: int) -> bool:
        if self.is_full():
            return False

        node = Node(value)
        if self.size == 0:
            self.head = self.tail = node
        else:
            self.tail.next = self.tail = node

        self.size += 1

        return True

    def de_queue(self) -> bool:
        if self.is_empty():
            return False

        self.head = self.head.next
        self.size -= 1

        return True

    def front(self) -> int:
        return -1 if self.is_empty() else self.head.val

    def rear(self) -> int:
        return -1 if self.is_empty() else self.tail.val

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.capacity == self.size
