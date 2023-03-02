import unittest

from arrays.StringCompression import compress


class MyTestCase(unittest.TestCase):
    def test_compress(self):
        self.assertEqual(6, compress(self, ["a", "a", "b", "b", "c", "c", "c"]))

    def test_compress_1(self):
        self.assertEqual(1, compress(self, ["a"]))

    def test_compress_2(self):
        self.assertEqual(4, compress(self, ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))

    def test_compress_3(self):
        chars = ["a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b",
                 "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c", "c", "c", "c", "c",
                 "c", "c", "c", "c", "c", "c", "c", "c", "c"]
        self.assertEqual(8, compress(self, chars))
        self.assertEqual(["a", "6", "b", "2", "1", "c", "1", "4"], chars)

    def test_compress_4(self):
        chars = ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]
        self.assertEqual(3, compress(self, chars))
        self.assertEqual(["o", "1", "0"], chars)

    def test_compress_5(self):
        chars = ["p", "p", "p", "p", "m", "m", "b", "b", "b", "b", "b", "u", "u", "r", "r", "u", "n", "n", "n", "n",
                 "n", "n", "n", "n", "n", "n", "n", "u", "u", "u", "u", "a", "a", "u", "u", "r", "r", "r", "s", "s",
                 "a", "a", "y", "y", "y", "g", "g", "g", "g", "g"]
        self.assertEqual(30, compress(self, chars))
        self.assertEqual(
            ["p", "4", "m", "2", "b", "5", "u", "2", "r", "2", "u", "n", "1", "1", "u", "4", "a", "2", "u", "2", "r",
             "3", "s", "2", "a", "2", "y", "3", "g", "5"], chars)

    def test_compress_6(self):
        chars = ["u", "n", "n", "n", "n",
                 "n", "n", "n", "n", "n", "n", "n", "u", "u", "u", "u", "a", "a", "u", "u", "r", "r", "r", "s", "s",
                 "a", "a", "y", "y", "y", "g", "g", "g", "g", "g"]
        self.assertEqual(20, compress(self, chars))
        self.assertEqual(
            ["u", "n", "1", "1", "u", "4", "a", "2", "u", "2", "r",
             "3", "s", "2", "a", "2", "y", "3", "g", "5"], chars)

    def test_compress_7(self):
        chars = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
        self.assertEqual(4, compress(self, chars))
        self.assertEqual(["a", "1", "0", "0"], chars)


if __name__ == '__main__':
    unittest.main()
