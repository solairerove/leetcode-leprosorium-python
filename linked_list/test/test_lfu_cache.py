import unittest

from linked_list.LFUCache import LFUCache


class MyTestCase(unittest.TestCase):
    def test_lfu(self):
        lfu = LFUCache(2)
        lfu.put(1, 1)  # cache=[1,_], cnt(1)=1
        lfu.put(2, 2)  # cache=[2,1], cnt(2)=1, cnt(1)=1
        self.assertEqual(1, lfu.get(1))
        # cache=[1,2], cnt(2)=1, cnt(1)=2
        lfu.put(3, 3)  # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
        # cache=[3,1], cnt(3)=1, cnt(1)=2
        self.assertEqual(-1, lfu.get(2))
        self.assertEqual(3, lfu.get(3))
        # cache=[3,1], cnt(3)=2, cnt(1)=2
        lfu.put(4, 4)  # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
        # cache=[4,3], cnt(4)=1, cnt(3)=2
        self.assertEqual(-1, lfu.get(1))
        self.assertEqual(3, lfu.get(3))
        # cache=[3,4], cnt(4)=1, cnt(3)=3
        self.assertEqual(4, lfu.get(4))
        # cache=[4,3], cnt(4)=2, cnt(3)=3


if __name__ == '__main__':
    unittest.main()
