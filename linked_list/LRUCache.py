class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key to node map

        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert_at_head(self, node: Node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert_at_head(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert_at_head(self.cache[key])

        if len(self.cache) > self.cap:
            node = self.tail.prev
            self.remove(node)
            del self.cache[node.key]
