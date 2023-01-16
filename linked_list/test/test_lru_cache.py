import unittest

from linked_list.LRUCache import LRUCache


class MyTestCase(unittest.TestCase):
    def test_lru_cache(self):
        lru_cache = LRUCache(2)
        lru_cache.put(1, 1)  # cache is {1=1}
        lru_cache.put(2, 2)  # cache is {1=1, 2=2}
        self.assertEqual(1, lru_cache.get(1))  # return 1
        lru_cache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        self.assertEqual(-1, lru_cache.get(2))  # returns -1 (not found)
        lru_cache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        self.assertEqual(-1, lru_cache.get(1))  # return -1 (not found)
        self.assertEqual(3, lru_cache.get(3))  # return 3
        self.assertEqual(4, lru_cache.get(4))  # return 4


if __name__ == '__main__':
    unittest.main()
