import unittest

from arrays.MeetingRoomsII import min_meeting_rooms


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(2, min_meeting_rooms(self, intervals=[[0, 30], [5, 10], [15, 20]]))

    def test_something_1(self):
        self.assertEqual(1, min_meeting_rooms(self, intervals=[[7, 10], [2, 4]]))

    def test_something_2(self):
        self.assertEqual(2, min_meeting_rooms(self, intervals=[[9, 10], [4, 9], [4, 17]]))


if __name__ == '__main__':
    unittest.main()
