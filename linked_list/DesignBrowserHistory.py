class Node:

    def __init__(self, val: str):
        self.val = val
        self.prev, self.nxt = None, None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head, self.tail = Node("-1"), Node("-1")
        self.head.nxt, self.tail.prev = self.tail, self.head

        self.page = Node(homepage)
        self.page.prev, self.page.nxt = self.head, self.tail
        self.head.nxt = self.tail.prev = self.page

    def visit(self, url: str) -> None:
        back_history = self.page
        self.page = Node(url)

        self.page.prev, self.page.nxt = self.head, back_history
        self.head.nxt = back_history.prev = self.page

    def back(self, steps: int) -> str:
        curr = self.page
        while curr and steps > 0 and curr.nxt != self.tail:
            curr, steps = curr.nxt, steps - 1

        self.page = curr

        return self.page.val

    def forward(self, steps: int) -> str:
        curr = self.page  # can use it actually
        while curr and steps > 0 and curr.prev != self.head:
            curr, steps = curr.prev, steps - 1

        self.page = curr

        return self.page.val
