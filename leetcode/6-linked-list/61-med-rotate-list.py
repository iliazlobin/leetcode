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

    def test_rotateRight_example1(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        result = self.solution.rotateRight(head, 2)
        self.assertEqual(linked_list_to_list(result), [4, 5, 1, 2, 3])

    def test_rotateRight_example2(self):
        head = list_to_linked_list([0, 1, 2])
        result = self.solution.rotateRight(head, 4)
        self.assertEqual(linked_list_to_list(result), [2, 0, 1])

    def test_rotateRight_empty(self):
        head = list_to_linked_list([])
        result = self.solution.rotateRight(head, 0)
        self.assertEqual(linked_list_to_list(result), [])

    def test_rotateRight_single_node(self):
        head = list_to_linked_list([1])
        result = self.solution.rotateRight(head, 0)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_rotateRight_single_node(self):
        head = list_to_linked_list([1])
        result = self.solution.rotateRight(head, 1)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_rotateRight_large_k(self):
        head = list_to_linked_list([1, 2, 3])
        result = self.solution.rotateRight(head, 2000000000)
        self.assertEqual(linked_list_to_list(result), [2, 3, 1])


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        dummy = ListNode(0, head)

        first = dummy.next
        size = 0
        while first:
            first = first.next
            size += 1

        for _ in range(k % size):
            head = head.next if head.next else dummy.next

        end = dummy.next
        while head.next:
            head = head.next
            end = end.next

        if not end.next:
            return dummy.next

        start = end.next
        end.next = None

        head.next = dummy.next

        return start


if __name__ == "__main__":
    unittest.main()
