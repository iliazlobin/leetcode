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

    def test_addTwoNumbers(self):
        l1 = list_to_linked_list([2, 4, 3])
        l2 = list_to_linked_list([5, 6, 4])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [7, 0, 8])

        l1 = list_to_linked_list([0])
        l2 = list_to_linked_list([0])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [0])

        l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = list_to_linked_list([9, 9, 9, 9])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [8, 9, 9, 9, 0, 0, 0, 1])

        l1 = list_to_linked_list([2, 4, 9])
        l2 = list_to_linked_list([5, 6, 4, 9])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [7, 0, 4, 0, 1])


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        first = prev = ListNode()
        while l1 and l2:
            sum = l1.val + l2.val
            withCarry = sum + carry
            node = ListNode(withCarry % 10)
            if prev:
                prev.next = node
            prev = node
            carry = 1 if withCarry >= 10 else 0
            l1 = l1.next
            l2 = l2.next

        l = l1 if l1 else l2
        while l:
            withCarry = l.val + carry
            node = ListNode(withCarry % 10)
            if prev:
                prev.next = node
            prev = node
            carry = 1 if withCarry >= 10 else 0
            l = l.next

        if carry > 0:
            node = ListNode(1)
            if prev:
                prev.next = node

        return first.next


if __name__ == "__main__":
    unittest.main()
