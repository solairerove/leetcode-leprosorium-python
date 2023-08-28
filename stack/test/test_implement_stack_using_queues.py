import unittest

from stack.ImplementStackUsingQueues import MyStack


class MyTestCase(unittest.TestCase):
    def test_implement_stack_using_queues(self):
        my_stack = MyStack()
        my_stack.push(1)
        my_stack.push(2)
        self.assertEqual(2, my_stack.top())
        self.assertEqual(2, my_stack.pop())
        self.assertEqual(False, my_stack.empty())


if __name__ == '__main__':
    unittest.main()
