import unittest

from dynamic_programming.EditDistance import min_distance_naive_recursive, min_distance_top_down


class MyTestCase(unittest.TestCase):
    def test_min_distance(self):
        self.assertEqual(3, min_distance_naive_recursive(self, "horse", "ros"))
        self.assertEqual(3, min_distance_top_down(self, "horse", "ros"))

    def test_min_distance_1(self):
        self.assertEqual(5, min_distance_naive_recursive(self, "intention", "execution"))
        self.assertEqual(5, min_distance_top_down(self, "intention", "execution"))


if __name__ == '__main__':
    unittest.main()
