import unittest

from linked_list.ListNode import ListNode
from linked_list.RemoveLinkedListElements import remove_elements


class MyTestCase(unittest.TestCase):
    def test_remove_elements(self):
        head = ListNode(
            val=1,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=6,
                    next=ListNode(
                        val=3,
                        next=ListNode(
                            val=4,
                            next=ListNode(
                                val=5,
                                next=ListNode(
                                    val=6
                                )
                            )
                        )
                    )
                )
            )
        )

        res = remove_elements(self, head, 6)
        arr = []
        while res:
            arr.append(res.val)
            res = res.next

        self.assertEqual([1, 2, 3, 4, 5], arr)

    def test_remove_elements_1(self):
        self.assertEqual(None, remove_elements(self, None, 1))

    def test_remove_elements_2(self):
        head = ListNode(
            val=7,
            next=ListNode(
                val=7,
                next=ListNode(
                    val=7,
                    next=ListNode(
                        val=7
                    )
                )
            )
        )

        res = remove_elements(self, head, 7)
        arr = []
        while res:
            arr.append(res.val)
            res = res.next

        self.assertEqual([], arr)


if __name__ == '__main__':
    unittest.main()
