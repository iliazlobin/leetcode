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
        print()


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        print()


if __name__ == "__main__":
    unittest.main()
