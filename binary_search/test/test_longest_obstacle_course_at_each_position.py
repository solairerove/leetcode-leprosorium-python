import unittest

from binary_search.FindTheLongestValidObstacleCourseAtEachPosition import longest_obstacle_course_at_each_position


class MyTestCase(unittest.TestCase):
    def test_longest_obstacle_course_at_each_position(self):
        self.assertEqual([1, 2, 3, 3], longest_obstacle_course_at_each_position(self, [1, 2, 3, 2]))

    def test_longest_obstacle_course_at_each_position_1(self):
        self.assertEqual([1, 2, 1], longest_obstacle_course_at_each_position(self, [2, 2, 1]))

    def test_longest_obstacle_course_at_each_position_2(self):
        self.assertEqual([1, 1, 2, 3, 2, 2], longest_obstacle_course_at_each_position(self, [3, 1, 5, 6, 4, 2]))


if __name__ == '__main__':
    unittest.main()
