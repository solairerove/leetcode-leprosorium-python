import unittest

from graphs.LargestColorValueInADirectedGraph import largest_path_value


class MyTestCase(unittest.TestCase):
    def test_largest_path_value(self):
        self.assertEqual(3, largest_path_value(self, "abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]))

    def test_largest_path_value_1(self):
        self.assertEqual(-1, largest_path_value(self, "a", [[0, 0]]))


if __name__ == '__main__':
    unittest.main()
