import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.solution = Solution()
        self.solution = NeetCodeSolution()

    def get_list_values(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values

    def test_reverseList(self):
        head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
        result = self.solution.reverseList(head)
        expected = [3, 2, 1, 0]
        self.assertEqual(self.get_list_values(result), expected)

        head = None
        result = self.solution.reverseList(head)
        expected = []
        self.assertEqual(self.get_list_values(result), expected)


# Definition for singly-linked list.
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


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not isinstance(head, ListNode):
            return None
        values = []
        while head.next:
            values.append(head.val)
            head = head.next
        values.append(head.val)
        values.reverse()
        reverse_list = ListNode(values[0])
        for vi, v in enumerate(values):
            if vi == 0:
                continue
            reverse_list.append(v)
        return reverse_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class NeetCodeSolution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            node = ListNode(curr.val)
            node.next = prev
            # curr.next = prev
            prev = node
            curr = temp
        return prev


if __name__ == "__main__":
    unittest.main()
