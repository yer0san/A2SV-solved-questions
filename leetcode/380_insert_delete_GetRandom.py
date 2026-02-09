import random
class RandomizedSet:

    def __init__(self):
        self.RandomisedSet = set()

    def insert(self, val: int) -> bool:
        if val not in self.RandomisedSet:
            self.RandomisedSet.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.RandomisedSet:
            self.RandomisedSet.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.RandomisedSet))
