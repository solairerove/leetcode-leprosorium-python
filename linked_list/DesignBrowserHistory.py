class Node:

    def __init__(self, val: str):
        self.val = val
        self.prev = self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)

    def visit(self, url: str) -> None:
        node = Node(url)
        node.prev = self.head
        self.head.next = self.head = node

    def back(self, steps: int) -> str:
        while steps > 0 and self.head.prev:
            self.head, steps = self.head.prev, steps - 1

        return self.head.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.head.next:
            self.head, steps = self.head.next, steps - 1

        return self.head.val
