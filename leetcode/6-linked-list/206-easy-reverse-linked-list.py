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

    def test_reverseList(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        result = self.solution.reverseList(head)
        self.assertEqual(linked_list_to_list(result), [5, 4, 3, 2, 1])

        head = list_to_linked_list([1, 2])
        result = self.solution.reverseList(head)
        self.assertEqual(linked_list_to_list(result), [2, 1])

        head = list_to_linked_list([])
        result = self.solution.reverseList(head)
        self.assertEqual(linked_list_to_list(result), [])


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev


if __name__ == "__main__":
    unittest.main()
