import unittest

from hash_table.DesignHashMap import MyHashMap


class MyTestCase(unittest.TestCase):
    def test_design_hash_map(self):
        my_hash_map = MyHashMap()
        my_hash_map.put(1, 1)  # The map is now [[1,1]]
        my_hash_map.put(2, 2)  # The map is now [[1,1], [2,2]]
        self.assertEqual(1, my_hash_map.get(1))  # return 1, The map is now [[1,1], [2,2]]
        self.assertEqual(-1, my_hash_map.get(3))  # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
        my_hash_map.put(2, 1)  # The map is now [[1,1], [2,1]] (i.e., update the existing value)
        self.assertEqual(1, my_hash_map.get(2))  # return 1, The map is now [[1,1], [2,1]]
        my_hash_map.remove(2)  # remove the mapping for 2, The map is now [[1,1]]
        self.assertEqual(-1, my_hash_map.get(2))  # return -1 (i.e., not found), The map is now [[1,1]]


if __name__ == '__main__':
    unittest.main()
