import unittest

from arrays.MajorityElementII import majority_element


class MyTestCase(unittest.TestCase):
    def test_majority_element_ii(self):
        self.assertEqual([3], majority_element(self, [3, 2, 3]))

    def test_majority_element_ii_1(self):
        self.assertEqual([1], majority_element(self, [1]))

    def test_majority_element_ii_2(self):
        self.assertEqual([1, 2], majority_element(self, [1, 2]))


if __name__ == '__main__':
    unittest.main()
