import unittest

from hash_table.DesignHashSet import MyHashSet


class MyTestCase(unittest.TestCase):
    def test_design_hash_set(self):
        my_hash_set = MyHashSet()
        my_hash_set.add(1)
        my_hash_set.add(2)
        self.assertEqual(True, my_hash_set.contains(1))
        self.assertEqual(False, my_hash_set.contains(3))
        self.assertEqual(True, my_hash_set.contains(2))
        my_hash_set.add(2)
        self.assertEqual(True, my_hash_set.contains(2))
        self.assertEqual(True, my_hash_set.contains(2))
        my_hash_set.remove(2)
        my_hash_set.contains(2)
        self.assertEqual(False, my_hash_set.contains(2))


if __name__ == '__main__':
    unittest.main()
