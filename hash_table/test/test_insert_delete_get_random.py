import unittest

from hash_table.InsertDeleteGetRandom import RandomizedSet


class MyTestCase(unittest.TestCase):

    def test_insert_delete_get_random_set(self):
        random_set = RandomizedSet()
        self.assertEqual(True, random_set.insert(1))
        self.assertEqual(False, random_set.remove(2))
        self.assertEqual(True, random_set.insert(2))
        self.assertEqual(True, random_set.get_random() in [1, 2])
        self.assertEqual(True, random_set.remove(1))
        self.assertEqual(False, random_set.insert(2))
        self.assertEqual(2, random_set.get_random())
        self.assertEqual(2, random_set.get_random())


if __name__ == '__main__':
    unittest.main()
