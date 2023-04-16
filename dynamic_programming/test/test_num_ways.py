import unittest

from dynamic_programming.NumberOfWaysToFormATargetStringGivenADictionary import num_ways_top_down


class MyTestCase(unittest.TestCase):
    def test_num_ways(self):
        self.assertEqual(6, num_ways_top_down(self, ["acca", "bbbb", "caca"], "aba"))

    def test_num_ways_1(self):
        self.assertEqual(4, num_ways_top_down(self, ["abba", "baab"], "bab"))


if __name__ == '__main__':
    unittest.main()
