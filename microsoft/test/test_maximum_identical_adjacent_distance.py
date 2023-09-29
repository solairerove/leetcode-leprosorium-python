import unittest

from microsoft.MaxDistanceBetweenSameElements import maximum_identical_adjacent_distance


class MyTestCase(unittest.TestCase):
    def test_maximum_identical_adjacent_distance(self):
        self.assertEqual(7, maximum_identical_adjacent_distance(self, "aakmaakmakda"))

    def test_maximum_identical_adjacent_distance_1(self):
        self.assertEqual(1, maximum_identical_adjacent_distance(self, "aaa"))

    def test_maximum_identical_adjacent_distance_2(self):
        self.assertEqual(-1, maximum_identical_adjacent_distance(self, "civic"))


if __name__ == '__main__':
    unittest.main()
