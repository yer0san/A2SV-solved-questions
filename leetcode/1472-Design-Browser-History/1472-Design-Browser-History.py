class Node:

    def __init__(self, url: str):
        self.val = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        node = Node(homepage)
        self.active = node
        self.activeon = 1
        self.head = node
        self.tail = self.active
        self.length = 1

    def visit(self, url: str) -> None:
        node = Node(url)
        self.active.next = node
        node.prev = self.active
        self.active = node
        self.active.next = None
        self.activeon += 1
        self.length = self.activeon
        self.tail = self.active

    def back(self, steps: int) -> str:
        if self.activeon - steps <= 1:
            self.active = self.head
            self.activeon = 1
            return self.active.val

        for _ in range(steps):
            self.active = self.active.prev
            self.activeon -= 1
        return self.active.val

    def forward(self, steps: int) -> str:
        if steps + self.activeon >= self.length:
            self.active = self.tail
            self.activeon = self.length
            return self.active.val

        for _ in range(steps):
            self.active = self.active.next
            self.activeon += 1
        return self.active.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)