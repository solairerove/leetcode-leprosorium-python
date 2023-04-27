import unittest

from maths.BulbSwitcher import bulb_switch


class MyTestCase(unittest.TestCase):
    def test_bulb_switch(self):
        self.assertEqual(1, bulb_switch(3))

    def test_bulb_switch_1(self):
        self.assertEqual(0, bulb_switch(0))

    def test_bulb_switch_2(self):
        self.assertEqual(1, bulb_switch(1))

    def test_bulb_switch_4(self):
        self.assertEqual(2, bulb_switch(4))

    def test_bulb_switch_5(self):
        self.assertEqual(2, bulb_switch(6))

    def test_bulb_switch_6(self):
        self.assertEqual(3, bulb_switch(9))


if __name__ == '__main__':
    unittest.main()
