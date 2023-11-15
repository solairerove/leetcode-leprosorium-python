import unittest

from greedy.MaximumElementAfterDecreasingAndRearranging import maximum_element_after_decrementing_and_rearranging


class MyTestCase(unittest.TestCase):
    def test_maximum_element_after_decrementing_and_rearranging(self):
        self.assertEqual(2, maximum_element_after_decrementing_and_rearranging(self, arr=[2, 2, 1, 2, 1]))

    def test_maximum_element_after_decrementing_and_rearranging_1(self):
        self.assertEqual(3, maximum_element_after_decrementing_and_rearranging(self, arr=[100, 1, 1000]))


if __name__ == '__main__':
    unittest.main()
