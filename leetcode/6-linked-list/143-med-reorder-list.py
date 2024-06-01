import unittest
from collections import Counter
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(lst):
    dummy = ListNode(0)
    ptr = dummy
    for i in lst:
        ptr.next = ListNode(i)
        ptr = ptr.next
    return dummy.next


def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rearrangeLinkedList(self):
        head = list_to_linked_list([1, 2, 3, 4])
        self.solution.reorderList(head)
        self.assertEqual(linked_list_to_list(head), [1, 4, 2, 3])

        head = list_to_linked_list([1, 2, 3, 4, 5])
        self.solution.reorderList(head)
        self.assertEqual(linked_list_to_list(head), [1, 5, 2, 4, 3])


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        backward = slow.next
        prev = slow.next = None
        while backward:
            temp = backward.next
            backward.next = prev
            prev = backward
            backward = temp

        forward, backward = head, prev
        while backward:
            forwardTmp, backwardTmp = forward.next, backward.next
            forward.next = backward
            backward.next = forwardTmp
            forward = forwardTmp
            backward = backwardTmp


if __name__ == "__main__":
    unittest.main()
