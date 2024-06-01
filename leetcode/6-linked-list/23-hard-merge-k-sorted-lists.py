import sys
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

    def test_mergeKLists(self):
        lists = [list_to_linked_list(lst) for lst in [[1, 4, 5], [1, 3, 4], [2, 6]]]
        result = self.solution.mergeKLists(lists)
        self.assertEqual(linked_list_to_list(result), [1, 1, 2, 3, 4, 4, 5, 6])

        lists = []
        result = self.solution.mergeKLists(lists)
        self.assertEqual(linked_list_to_list(result), [])

        lists = [list_to_linked_list(lst) for lst in [[]]]
        result = self.solution.mergeKLists(lists)
        self.assertEqual(linked_list_to_list(result), [])


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeLists(l1, l2))
            lists = mergedLists

        return lists[0]

    def mergeLists(self, l1, l2):
        tail = start = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return start.next


if __name__ == "__main__":
    unittest.main()
