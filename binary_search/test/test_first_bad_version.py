import unittest

from binary_search.FirstBadVersion import first_bad_version


class MyTestCase(unittest.TestCase):
    def test_first_bad_version(self):
        self.assertEqual(4, first_bad_version(self, 5, 4))

    def test_first_bad_version_1(self):
        self.assertEqual(1, first_bad_version(self, 1, 1))


if __name__ == '__main__':
    unittest.main()
