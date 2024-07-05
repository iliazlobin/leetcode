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

    def test_deleteDuplicates_example1(self):
        head = self.list_to_linkedlist([1, 2, 3, 3, 4, 4, 5])
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedlist_to_list(result), [1, 2, 5])

    def test_deleteDuplicates_example2(self):
        head = self.list_to_linkedlist([1, 1, 1, 2, 3])
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedlist_to_list(result), [2, 3])

    def test_deleteDuplicates_example3(self):
        head = self.list_to_linkedlist([1, 1])
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedlist_to_list(result), [])

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        s = set()

        cur = dummy
        prev = None
        while head:
            if head.val not in s:
                s.add(head.val)
                prev = cur
                cur.next = head
                cur = cur.next
            else:
                cur = prev
                cur.next = head.next
            head = head.next

        return dummy.next


if __name__ == "__main__":
    unittest.main()
