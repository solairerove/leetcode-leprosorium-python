import unittest

from sliding_window.FrequencyOfTheMostFrequentElement import max_frequency


class MyTestCase(unittest.TestCase):
    def test_max_frequency(self):
        self.assertEqual(3, max_frequency(self, nums=[1, 2, 4], k=5))

    def test_max_frequency_1(self):
        self.assertEqual(2, max_frequency(self, nums=[1, 4, 8, 13], k=5))

    def test_max_frequency_2(self):
        self.assertEqual(1, max_frequency(self, nums=[3, 9, 6], k=2))


if __name__ == '__main__':
    unittest.main()
