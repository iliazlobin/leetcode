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
        # self.solution = Solution()
        self.solution = NeetCodeSolution()

    def test_mergeTwoLists(self):
        list1 = list_to_linked_list([1, 2, 4])
        list2 = list_to_linked_list([1, 3, 4, 5, 6])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 1, 2, 3, 4, 4, 5, 6])

        list1 = list_to_linked_list([])
        list2 = list_to_linked_list([])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [])

        list1 = list_to_linked_list([])
        list2 = list_to_linked_list([0])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [0])


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        start = ListNode()
        node, prev = None, start

        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    node = ListNode(list1.val)
                    list1 = list1.next
                else:
                    node = ListNode(list2.val)
                    list2 = list2.next
            elif list1 and not list2:
                node = ListNode(list1.val)
                list1 = list1.next
            elif not list1 and list2:
                node = ListNode(list2.val)
                list2 = list2.next
            else:
                return
            prev.next = node
            prev = node
        return start.next


class NeetCodeSolution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next


if __name__ == "__main__":
    unittest.main()
