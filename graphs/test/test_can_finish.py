import unittest

from graphs.CourseSchedule import can_finish


class MyTestCase(unittest.TestCase):
    def test_can_finish(self):
        self.assertEqual(True, can_finish(self, 2, [[1, 0]]))

    def test_can_finish_1(self):
        self.assertEqual(False, can_finish(self, 2, [[1, 0], [0, 1]]))


if __name__ == '__main__':
    unittest.main()
