import unittest

from arrays.CanPlaceFlowers import can_place_flowers


class MyTestCase(unittest.TestCase):
    def test_can_place_flowers(self):
        self.assertEqual(True, can_place_flowers(self, [1, 0, 0, 0, 1], 1))

    def test_can_place_flowers_1(self):
        self.assertEqual(False, can_place_flowers(self, [1, 0, 0, 0, 1], 2))

    def test_can_place_flowers_2(self):
        self.assertEqual(True, can_place_flowers(self, [0, 0, 1, 0, 1], 1))

    def test_can_place_flowers_3(self):
        self.assertEqual(True, can_place_flowers(self, [1, 0, 0, 0, 1, 0, 0], 2))

    def test_can_place_flowers_4(self):
        self.assertEqual(True, can_place_flowers(self, [1], 0))


if __name__ == '__main__':
    unittest.main()
