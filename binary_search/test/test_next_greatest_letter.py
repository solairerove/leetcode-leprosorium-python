import unittest

from binary_search.FindSmallestLetterGreaterThanTarget import next_greatest_letter_linear


class MyTestCase(unittest.TestCase):
    def test_next_greatest_letter(self):
        self.assertEqual("c", next_greatest_letter_linear(self, ["c", "f", "j"], "a"))

    def test_next_greatest_letter_1(self):
        self.assertEqual("f", next_greatest_letter_linear(self, ["c", "f", "j"], "c"))

    def test_next_greatest_letter_2(self):
        self.assertEqual("x", next_greatest_letter_linear(self, ["x", "x", "y", "y"], "z"))


if __name__ == '__main__':
    unittest.main()
