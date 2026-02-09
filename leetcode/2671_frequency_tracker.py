class FrequencyTracker:

    def __init__(self):
        self.arr = []
        self.freq = defaultdict(int)
        self.count = defaultdict(int)

    def add(self, number: int) -> None:
        self.arr.append(number)
        self.count[self.freq[number]] -= 1
        if self.count[self.freq[number]] <= 0:
            del self.count[self.freq[number]]
        self.freq[number] += 1
        self.count[self.freq[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.freq[number] > 0:
            self.arr.remove(number)
            self.count[self.freq[number]] -= 1
            if self.count[self.freq[number]] <= 0:
                del self.count[self.freq[number]]
            self.freq[number] -= 1
            self.count[self.freq[number]] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        return True if frequency in self.count else False

