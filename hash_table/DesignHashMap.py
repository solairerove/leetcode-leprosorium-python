class Bucket:

    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v

        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


# O(N / K) time || O(K + M) space
# N - size of all keys
# M - size of unique keys
# K - predefined size of buckets in map
class MyHashMap:

    def __init__(self):
        self.key_space = 2069
        self.ht = [Bucket() for _ in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.key_space
        self.ht[hash_key].update(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.key_space

        return self.ht[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.key_space
        self.ht[hash_key].remove(key)
