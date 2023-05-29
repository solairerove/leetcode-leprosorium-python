import unittest

from greedy.DesignParkingSystem import ParkingSystem


class MyTestCase(unittest.TestCase):
    def test_parking_system(self):
        parking_system = ParkingSystem(1, 1, 0)
        self.assertEqual(True, parking_system.add_car(1))
        self.assertEqual(True, parking_system.add_car(2))
        self.assertEqual(False, parking_system.add_car(3))
        self.assertEqual(False, parking_system.add_car(1))


if __name__ == '__main__':
    unittest.main()
