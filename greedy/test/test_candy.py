import unittest

from greedy.Candy import candy


class MyTestCase(unittest.TestCase):
    def test_candy(self):
        self.assertEqual(5, candy(self, [1, 0, 2]))

    def test_candy_1(self):
        self.assertEqual(4, candy(self, [1, 2, 2]))


if __name__ == '__main__':
    unittest.main()
