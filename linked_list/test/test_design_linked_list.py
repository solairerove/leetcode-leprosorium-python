import unittest

from linked_list.DesignLinkedList import MyLinkedList


class MyTestCase(unittest.TestCase):
    def test_test_design_linked_list(self):
        my_linked_list = MyLinkedList()
        my_linked_list.add_at_head(1)
        my_linked_list.add_at_tail(3)
        my_linked_list.add_at_index(1, 2)  # linked list becomes 1 -> 2 -> 3
        self.assertEqual(2, my_linked_list.get(1))
        my_linked_list.delete_at_index(1)  # now the linked list is 1 -> 3
        self.assertEqual(3, my_linked_list.get(1))


if __name__ == '__main__':
    unittest.main()
