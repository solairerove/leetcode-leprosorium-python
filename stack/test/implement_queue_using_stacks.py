import unittest

from stack.ImplementQueueUsingStacks import MyQueue


class MyTestCase(unittest.TestCase):
    def test_implement_queue_using_stacks(self):
        my_queue = MyQueue()
        my_queue.push(1)
        my_queue.push(2)
        self.assertEqual(1, my_queue.peek())
        self.assertEqual(1, my_queue.pop())
        self.assertEqual(False, my_queue.empty())


if __name__ == '__main__':
    unittest.main()
