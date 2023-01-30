import unittest

from linked_list.DesignCircularDeque import MyCircularDeque


class MyTestCase(unittest.TestCase):
    def test_design_circular_deque(self):
        my_circular_deque = MyCircularDeque(3)
        self.assertEqual(True, my_circular_deque.insert_last(1))
        self.assertEqual(True, my_circular_deque.insert_last(2))
        self.assertEqual(True, my_circular_deque.insert_front(3))
        self.assertEqual(False, my_circular_deque.insert_front(4))
        self.assertEqual(2, my_circular_deque.get_rear())
        self.assertEqual(True, my_circular_deque.is_full())
        self.assertEqual(True, my_circular_deque.delete_last())
        self.assertEqual(True, my_circular_deque.insert_front(4))
        self.assertEqual(4, my_circular_deque.get_front())


if __name__ == '__main__':
    unittest.main()
