from linked_list.RemoveNodesFromLinkedList import Sou
from linked_list.hello import Solution
from linked_list.listNode import ListNode


def testReverseEvenLengthGroups():
    head = ListNode(
        val=5,
        next=ListNode(
            val=2,
            next=ListNode(
                val=6,
                next=ListNode(
                    val=3,
                    next=ListNode(
                        val=9,
                        next=ListNode(
                            val=1,
                            next=ListNode(
                                val=7,
                                next=ListNode(
                                    val=3,
                                    next=ListNode(
                                        val=8,
                                        next=ListNode(
                                            val=4
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
    res = Solution.reverseEvenLengthGroups(head)
    arr = []
    while res:
        arr.append(res.val)
        res = res.next

    print(arr)
    assert arr == [5, 6, 2, 3, 9, 1, 4, 8, 3, 7], "Should be [5, 6, 2, 3, 9, 1, 4, 8, 3, 7]"


def testRemoveNodesFromLinkedList():
    head = ListNode(
        val=5,
        next=ListNode(
            val=2,
            next=ListNode(
                val=13,
                next=ListNode(
                    val=3,
                    next=ListNode(
                        val=8
                    )
                )
            )
        )
    )
    res = Sou.removeNodes(__name__, head)
    arr = []
    while res:
        arr.append(res.val)
        res = res.next

    print(arr)
    assert arr == [13, 8], "Should be [13, 8]"


if __name__ == '__main__':
    testReverseEvenLengthGroups()
    testRemoveNodesFromLinkedList()
    print("Everything passed")
