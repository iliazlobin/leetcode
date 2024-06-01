import unittest
from collections import Counter
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, val):
        new_node = ListNode(val)
        if self.next is None:
            self.next = new_node
            return
        last = self.next
        while last.next:
            last = last.next
        last.next = new_node


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isValid(self):
        print()


class Solution:
    def isValid(self, s: str) -> bool:
        print()


if __name__ == "__main__":
    unittest.main()
