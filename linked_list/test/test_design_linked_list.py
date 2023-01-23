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

    def test_test_design_linked_list_6(self):
        my_linked_list = MyLinkedList()
        my_linked_list.add_at_head(7)
        my_linked_list.add_at_head(2)
        my_linked_list.add_at_head(1)
        my_linked_list.add_at_index(3, 0)  # 1 -> 2 -> 7 -> 0
        my_linked_list.delete_at_index(2)  # 1 -> 2 -> 0
        my_linked_list.add_at_head(6)  # 6 -> 1 -> 2 -> 0
        my_linked_list.add_at_tail(4)  # 6 -> 1 -> 2 -> 0 -> 4
        self.assertEqual(4, my_linked_list.get(4))
        my_linked_list.add_at_head(4)  # 4 -> 6 -> 1 -> 2 -> 0 -> 4
        my_linked_list.add_at_index(5, 0)  # 4 -> 6 -> 1 -> 2 -> 0 -> 5 -> 4
        my_linked_list.add_at_head(6)  # 6 -> 4 -> 6 -> 1 -> 2 -> 0 -> 5 -> 4


if __name__ == '__main__':
    unittest.main()
