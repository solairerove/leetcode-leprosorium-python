import unittest

from linked_list.DesignCircularQueue import MyCircularQueue


class MyTestCase(unittest.TestCase):
    def test_design_circular_queue(self):
        my_circular_queue = MyCircularQueue(3)
        self.assertEqual(True, my_circular_queue.en_queue(1))
        self.assertEqual(True, my_circular_queue.en_queue(2))
        self.assertEqual(True, my_circular_queue.en_queue(3))
        self.assertEqual(False, my_circular_queue.en_queue(4))
        self.assertEqual(3, my_circular_queue.rear())
        self.assertEqual(True, my_circular_queue.is_full())
        self.assertEqual(True, my_circular_queue.de_queue())
        self.assertEqual(True, my_circular_queue.en_queue(4))
        self.assertEqual(4, my_circular_queue.rear())


if __name__ == '__main__':
    unittest.main()
