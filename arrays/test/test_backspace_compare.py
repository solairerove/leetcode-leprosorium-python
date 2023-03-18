import unittest

from arrays.BackspaceStringCompare import backspace_compare_two_pointers, backspace_compare_stack


class MyTestCase(unittest.TestCase):
    def test_backspace_compare(self):
        self.assertEqual(True, backspace_compare_two_pointers(self, "ab#c", "ad#c"))
        self.assertEqual(True, backspace_compare_stack(self, "ab#c", "ad#c"))

    def test_backspace_compare_1(self):
        self.assertEqual(True, backspace_compare_two_pointers(self, "ab##", "c#d#"))
        self.assertEqual(True, backspace_compare_stack(self, "ab##", "c#d#"))

    def test_backspace_compare_2(self):
        self.assertEqual(False, backspace_compare_two_pointers(self, "a#c", "b"))
        self.assertEqual(False, backspace_compare_stack(self, "a#c", "b"))


if __name__ == '__main__':
    unittest.main()
