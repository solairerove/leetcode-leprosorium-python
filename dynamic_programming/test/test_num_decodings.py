import unittest

from dynamic_programming.DecodeWays import num_decodings


class MyTestCase(unittest.TestCase):
    def test_num_decodings(self):
        self.assertEqual(2, num_decodings(self, "12"))  

    def test_num_decodings_1(self):
        self.assertEqual(3, num_decodings(self, "226"))  

    def test_num_decodings_2(self):
        self.assertEqual(0, num_decodings(self, "06"))

    def test_num_decodings_3(self):
        self.assertEqual(5, num_decodings(self, "2125"))


if __name__ == '__main__':
    unittest.main()
