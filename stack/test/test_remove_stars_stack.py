import unittest

from stack.RemovingStarsFromAString import remove_stars_stack


class MyTestCase(unittest.TestCase):
    def test_remove_stars_stack(self):
        self.assertEqual("lecoe", remove_stars_stack(self, "leet**cod*e"))

    def test_remove_stars_stack_1(self):
        self.assertEqual("", remove_stars_stack(self, "erase*****"))


if __name__ == '__main__':
    unittest.main()
