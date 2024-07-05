import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def list_to_linkedlist(self, lst):
        # Helper method to convert a list to a linked list
        head = ListNode(0)  # Dummy head
        current = head
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return head.next

    def linkedlist_to_list(self, head):
        # Helper method to convert a linked list back to a list
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst

    def test_partition_example1(self):
        head = self.list_to_linkedlist([1, 4, 3, 2, 5, 2])
        result = self.solution.partition(head, 3)
        self.assertEqual(self.linkedlist_to_list(result), [1, 2, 2, 4, 3, 5])

    def test_partition_example2(self):
        head = self.list_to_linkedlist([2, 1])
        result = self.solution.partition(head, 2)
        self.assertEqual(self.linkedlist_to_list(result), [1, 2])


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left = dummy
        rightStart = right = ListNode(0)
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next

        right.next = None
        left.next = rightStart.next

        return dummy.next


if __name__ == "__main__":
    unittest.main()
