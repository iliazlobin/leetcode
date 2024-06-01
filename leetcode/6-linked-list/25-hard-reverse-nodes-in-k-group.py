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

    def test_reverseKGroup(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        result = self.solution.reverseKGroup(head, 2)
        self.assertEqual(linked_list_to_list(result), [2, 1, 4, 3, 5])

        head = list_to_linked_list([1, 2, 3, 4, 5])
        result = self.solution.reverseKGroup(head, 3)
        self.assertEqual(linked_list_to_list(result), [3, 2, 1, 4, 5])


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse group
            prev = kth.next
            curr = groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


if __name__ == "__main__":
    unittest.main()
