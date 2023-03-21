import unittest

from arrays.MajorityElement import majority_element_hm


class MyTestCase(unittest.TestCase):
    def test_majority_element(self):
        self.assertEqual(3, majority_element_hm(self, [3, 2, 3]))

    def test_majority_element_1(self):
        self.assertEqual(2, majority_element_hm(self, [2, 2, 1, 1, 1, 2, 2]))


if __name__ == '__main__':
    unittest.main()
