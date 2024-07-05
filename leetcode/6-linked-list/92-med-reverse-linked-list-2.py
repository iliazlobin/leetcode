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

    def test_reverseBetween(self):
        # Test case 1
        head = self.list_to_linkedlist([1, 2, 3, 4, 5])
        result = self.solution.reverseBetween(head, 2, 4)
        self.assertEqual(self.linkedlist_to_list(result), [1, 4, 3, 2, 5])

        # Test case 2
        head = self.list_to_linkedlist([5])
        result = self.solution.reverseBetween(head, 1, 1)
        self.assertEqual(self.linkedlist_to_list(result), [5])

        head = self.list_to_linkedlist([3, 5])
        result = self.solution.reverseBetween(head, 1, 2)
        self.assertEqual(self.linkedlist_to_list(result), [5, 3])


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0, head)

        before = dummy
        position = 1
        while position < left:
            before = head
            head = head.next
            position += 1

        middle = head

        while position < right:
            head = head.next
            position += 1
        after = head.next
        head.next = None

        reverseMiddle = self.reverse(middle)
        before.next = reverseMiddle
        middle.next = after

        return dummy.next


if __name__ == "__main__":
    unittest.main()
