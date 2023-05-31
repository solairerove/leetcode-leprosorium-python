import unittest

from hash_table.DesignUndergroundSystem import UndergroundSystem


class MyTestCase(unittest.TestCase):
    def test_underground_system(self):
        underground_system = UndergroundSystem()
        underground_system.check_in(45, "Leyton", 3)
        underground_system.check_in(32, "Paradise", 8)
        underground_system.check_in(27, "Leyton", 10)
        underground_system.check_out(45, "Waterloo", 15)  # Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
        underground_system.check_out(27, "Waterloo", 20)  # Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
        underground_system.check_out(32, "Cambridge", 22)  # Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
        self.assertEqual(14.00000, underground_system.get_average_time("Paradise", "Cambridge"))  # return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
        self.assertEqual(11.00000, underground_system.get_average_time("Leyton", "Waterloo"))  # return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
        underground_system.check_in(10, "Leyton", 24)
        self.assertEqual(11.00000, underground_system.get_average_time("Leyton", "Waterloo"))
        underground_system.check_out(10, "Waterloo", 38)  # Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
        self.assertEqual(12.00000, underground_system.get_average_time("Leyton", "Waterloo"))  # return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12

    def test_underground_system_1(self):
        underground_system = UndergroundSystem()
        underground_system.check_in(10, "Leyton", 3)
        underground_system.check_out(10, "Paradise", 8)  # Customer 10 "Leyton" -> "Paradise" in 8-3 = 5
        self.assertEqual(5.00000, underground_system.get_average_time("Leyton", "Paradise"))

        underground_system.check_in(5, "Leyton", 10)
        underground_system.check_out(5, "Paradise", 16)  # Customer 5 "Leyton" -> "Paradise" in 16-10 = 6
        self.assertEqual(5.50000, underground_system.get_average_time("Leyton", "Paradise"))

        underground_system.check_in(2, "Leyton", 21)
        underground_system.check_out(2, "Paradise", 30)  # Customer 2 "Leyton" -> "Paradise" in 30-21 = 9
        self.assertEqual(6.666666666666667, underground_system.get_average_time("Leyton", "Paradise"))


if __name__ == '__main__':
    unittest.main()
