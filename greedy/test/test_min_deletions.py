import unittest

from greedy.MinimumDeletionsToMakeCharacterFrequenciesUnique import min_deletions


class MyTestCase(unittest.TestCase):
    def test_min_deletions(self):
        self.assertEqual(0, min_deletions(self, s="aab"))

    def test_min_deletions_1(self):
        self.assertEqual(2, min_deletions(self, s="aaabbbcc"))

    def test_min_deletions_2(self):
        self.assertEqual(2, min_deletions(self, s="ceabaacb"))


if __name__ == '__main__':
    unittest.main()
