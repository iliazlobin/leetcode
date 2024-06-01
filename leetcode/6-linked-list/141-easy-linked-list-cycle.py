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

    def test_hasCycle(self):
        head = list_to_linked_list([3, 2, 0, -4])
        head.next.next.next.next = head.next
        result = self.solution.hasCycle(head)
        self.assertEqual(result, True)

        head = list_to_linked_list([1, 2])
        head.next.next = head
        result = self.solution.hasCycle(head)
        self.assertEqual(result, True)

        head = list_to_linked_list([1])
        result = self.solution.hasCycle(head)
        self.assertEqual(result, False)


class OnSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()

        while head:
            if head.val in s:
                return True
            s.add(head.val)
            head = head.next
        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s, f = head, head

        while head:
            if s.val == f.val:
                return True
            s = s.next
            f = f.next
            if not f:
                return False
            f = f.next
        return False


if __name__ == "__main__":
    unittest.main()
