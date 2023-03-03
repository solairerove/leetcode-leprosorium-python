import unittest

from arrays.MeetingRooms import can_attend_meetings, can_attend_meetings_short


class MyTestCase(unittest.TestCase):
    def test_can_attend_meetings(self):
        self.assertEqual(False, can_attend_meetings(self, [[0, 30], [5, 10], [15, 20]]))
        self.assertEqual(False, can_attend_meetings_short(self, [[0, 30], [5, 10], [15, 20]]))

    def test_can_attend_meetings_1(self):
        self.assertEqual(True, can_attend_meetings(self, [[7, 10], [2, 4]]))
        self.assertEqual(True, can_attend_meetings_short(self, [[7, 10], [2, 4]]))


if __name__ == '__main__':
    unittest.main()
