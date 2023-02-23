import unittest

from dynamic_programming.UniquePaths import unique_paths_top_down, unique_paths_bottom_up


class MyTestCase(unittest.TestCase):
    def test_unique_paths(self):
        self.assertEqual(28, unique_paths_top_down(self, 3, 7))
        self.assertEqual(28, unique_paths_bottom_up(self, 3, 7))

    def test_unique_paths_1(self):
        self.assertEqual(3, unique_paths_top_down(self, 3, 2))
        self.assertEqual(3, unique_paths_bottom_up(self, 3, 2))


if __name__ == '__main__':
    unittest.main()
