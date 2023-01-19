import unittest

from linked_list.AddTwoNumbers import add_two_numbers
from linked_list.ListNode import ListNode


class MyTestCase(unittest.TestCase):
    def test_add_two_numbers(self):
        list1 = ListNode(
            val=2,
            next=ListNode(
                val=4,
                next=ListNode(
                    val=3
                )
            )
        )

        list2 = ListNode(
            val=5,
            next=ListNode(
                val=6,
                next=ListNode(
                    val=4
                )
            )
        )

        res = add_two_numbers(__name__, list1, list2)
        arr = []
        while res:
            arr.append(res.val)
            res = res.next

        self.assertEqual([7, 0, 8], arr)  


if __name__ == '__main__':
    unittest.main()
