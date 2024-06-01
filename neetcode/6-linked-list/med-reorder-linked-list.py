import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.solution = Solution()
        self.solution = NeetCodeSolution()

    def test_reorderList(self):
        # Test case 1
        head = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))
        self.solution.reorderList(head)
        expected = [2, 8, 4, 6]
        self.assertEqual(self.get_list_values(head), expected)

        # Test case 2
        head = ListNode(2, ListNode(4, ListNode(6, ListNode(8, ListNode(10)))))
        self.solution.reorderList(head)
        expected = [2, 10, 4, 8, 6]
        self.assertEqual(self.get_list_values(head), expected)

    def get_list_values(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:


class NeetCodeSolution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

if __name__ == "__main__":
    unittest.main()

