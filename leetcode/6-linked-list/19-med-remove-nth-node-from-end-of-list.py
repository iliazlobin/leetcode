import unittest
from collections import Counter
from typing import List, Optional

from sklearn import dummy


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

    def test_removeNthFromEnd(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        result = self.solution.removeNthFromEnd(head, 2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 5])

        head = list_to_linked_list([1])
        result = self.solution.removeNthFromEnd(head, 1)
        self.assertEqual(linked_list_to_list(result), [])

        head = list_to_linked_list([1, 2])
        result = self.solution.removeNthFromEnd(head, 1)
        self.assertEqual(linked_list_to_list(result), [1])


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0, head)
        left = start
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return start.next


if __name__ == "__main__":
    unittest.main()
