import unittest

from hash_table.InsertDeleteGetRandomDuplicatesAllowed import RandomizedCollection


class MyTestCase(unittest.TestCase):
    def test_insert_delete_get_random_duplicates_allowed(self):
        randomized_collection = RandomizedCollection()
        self.assertEqual(True, randomized_collection.insert(1))
        self.assertEqual(False, randomized_collection.insert(1))
        self.assertEqual(True, randomized_collection.insert(2))
        self.assertEqual(True, randomized_collection.get_random() in [1, 2])
        self.assertEqual(True, randomized_collection.remove(1))
        self.assertEqual(True, randomized_collection.get_random() in [1, 2])


if __name__ == '__main__':
    unittest.main()
