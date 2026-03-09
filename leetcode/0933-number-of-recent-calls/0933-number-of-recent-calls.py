class RecentCounter:

    def __init__(self):
        self.counter = []
        self.idx = 0

    def ping(self, t: int) -> int:
        self.counter.append(t)
        off = t-3000
        while self.counter[self.idx] < off:
            self.idx += 1
        return len(self.counter) - self.idx
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)