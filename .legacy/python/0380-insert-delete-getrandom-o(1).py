class RandomizedSet:

    # O(1) time
    def __init__(self):
        self.hashmap = {}
        self.array = []

    # O(1) time
    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.hashmap[val] = len(self.array)
        self.array.append(val)
        return True

    # O(1) time
    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        idx = self.hashmap[val]
        last = self.array[-1]
        self.array[idx] = last
        self.hashmap[last] = idx
        del self.hashmap[val]
        self.array.pop()
        return True

    # O(1) time
    def getRandom(self) -> int:
        return random.choice(self.array)