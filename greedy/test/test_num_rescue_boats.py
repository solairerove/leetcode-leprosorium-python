import unittest

from greedy.BoatsToSavePeople import num_rescue_boats_naive


class MyTestCase(unittest.TestCase):
    def test_num_rescue_boats(self):
        self.assertEqual(1, num_rescue_boats_naive(self, [1, 2], 3))

    def test_num_rescue_boats_1(self):
        self.assertEqual(3, num_rescue_boats_naive(self, [3, 2, 2, 1], 3))

    def test_num_rescue_boats_2(self):
        self.assertEqual(4, num_rescue_boats_naive(self, [3, 5, 3, 4], 5))

    def test_num_rescue_boats_3(self):
        self.assertEqual(2, num_rescue_boats_naive(self, [5, 1, 4, 2], 6))

    def test_num_rescue_boats_4(self):
        self.assertEqual(1, num_rescue_boats_naive(self, [2, 2], 6))

    def test_num_rescue_boats_5(self):
        self.assertEqual(2, num_rescue_boats_naive(self, [3,1,7], 7))


if __name__ == '__main__':
    unittest.main()
