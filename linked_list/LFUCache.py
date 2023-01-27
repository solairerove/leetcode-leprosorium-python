from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq_to_key = defaultdict(lambda: OrderedDict())
        self.key_to_freq = defaultdict(int)
        self.min_freq = 1

    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1

        freq = self.key_to_freq[key]
        self.key_to_freq[key] = freq + 1

        value = self.freq_to_key[freq][key]
        del self.freq_to_key[freq][key]
        self.freq_to_key[freq + 1][key] = value

        if self.min_freq == freq and not self.freq_to_key[freq]:
            self.min_freq += 1

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_freq:
            self.get(key)
            self.freq_to_key[self.key_to_freq[key]][key] = value
        else:
            self.capacity -= 1
            self.key_to_freq[key] = 1
            self.freq_to_key[1][key] = value
            if self.capacity < 0:
                self.capacity += 1
                k, v = self.freq_to_key[self.min_freq].popitem(False)
                del self.key_to_freq[k]
            self.min_freq = 1
