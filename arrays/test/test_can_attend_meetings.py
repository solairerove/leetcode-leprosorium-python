import unittest

from arrays.MeetingRooms import can_attend_meetings


class MyTestCase(unittest.TestCase):
    def test_can_attend_meetings(self):
        self.assertEqual(False, can_attend_meetings(self, [[0, 30], [5, 10], [15, 20]]))

    def test_can_attend_meetings_1(self):
        self.assertEqual(True, can_attend_meetings(self, [[7, 10], [2, 4]]))


if __name__ == '__main__':
    unittest.main()
