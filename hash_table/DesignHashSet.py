class MyHashSet:

    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.s = [None] * 8
        self.load_factor = float(2) / 3

    def hash(self, key) -> int:
        return key % self.capacity

    def add(self, key: int) -> None:
        if float(self.size) / self.capacity >= self.load_factor:
            self.capacity <<= 1
            new_set = [None] * self.capacity
            for i in range(self.capacity >> 1):
                if self.s[i] and self.s[i] != "==TOMBSTONE==":
                    n = self.hash(self.s[i])
                    while new_set[n] is not None:
                        n = (5 * n + 1) % self.capacity
                    new_set[n] = self.s[i]
            self.s = new_set

        h = self.hash(key)
        while self.s[h] is not None:
            if self.s[h] == key:
                return

            h = (5 * h + 1) % self.capacity
            if self.s[h] == "==TOMBSTONE==":
                break

        self.s[h] = key
        self.size += 1

    def remove(self, key: int) -> None:
        h = self.hash(key)
        while self.s[h] is not None:
            if self.s[h] == key:
                self.s[h] = "==TOMBSTONE=="
                self.size -= 1
                return

            h = (5 * h + 1) % self.capacity

    def contains(self, key: int) -> bool:
        h = self.hash(key)
        while self.s[h] is not None:
            if self.s[h] == key:
                return True

            h = (5 * h + 1) % self.capacity

        return False
