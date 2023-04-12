import unittest

from stack.SimplifyPath import simplify_path, simplify_path_os


class MyTestCase(unittest.TestCase):
    def test_simplify_path(self):
        self.assertEqual("/home", simplify_path(self, "/home/"))
        self.assertEqual("/home", simplify_path_os(self, "/home/"))

    def test_simplify_path_1(self):
        self.assertEqual("/", simplify_path(self, "/../"))
        self.assertEqual("/", simplify_path_os(self, "/../"))

    def test_simplify_path_2(self):
        self.assertEqual("/home/foo", simplify_path(self, "/home//foo/"))
        self.assertEqual("/home/foo", simplify_path_os(self, "/home//foo/"))


if __name__ == '__main__':
    unittest.main()
