import unittest

from dynamic_programming.NumberOfWaysOfCuttingAPizza import ways


class MyTestCase(unittest.TestCase):
    def test_ways(self):
        self.assertEqual(3, ways(self, ["A..", "AAA", "..."], 3))

    def test_ways_1(self):
        self.assertEqual(1, ways(self, ["A..", "AA.", "..."], 3))

    def test_ways_2(self):
        self.assertEqual(1, ways(self, ["A..", "A..", "..."], 1))


if __name__ == '__main__':
    unittest.main()
