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

    def test_mergeTwoLists(self):
        # Test case 1
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(5)))
        result = self.solution.mergeTwoLists(list1, list2)
        expected = [1, 1, 2, 3, 4, 5]
        self.assertEqual(self.get_list_values(result), expected)

        # Test case 2
        list1 = None
        list2 = ListNode(1, ListNode(2))
        result = self.solution.mergeTwoLists(list1, list2)
        expected = [1, 2]
        self.assertEqual(self.get_list_values(result), expected)

        # Test case 3
        list1 = None
        list2 = None
        result = self.solution.mergeTwoLists(list1, list2)
        expected = []
        self.assertEqual(self.get_list_values(result), expected)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        new_list = None
        new_head = None
        while True:
            min_val = None
            if list1 is None:
                min_val = list2.val
                list2 = list2.next
            elif list2 is None:
                min_val = list1.val
                list1 = list1.next
            else:
                val1 = list1.val
                val2 = list2.val
                # node = None
                if val1 <= val2:
                    min_val = val1
                    list1 = list1.next
                else:
                    min_val = val2
                    list2 = list2.next
            if new_list is None:
                new_list = ListNode(min_val)
                new_head = new_list
            else:
                new_head.next = ListNode(min_val)
                new_head = new_head.next
            if list1 is None and list2 is None:
                return new_list


class NeetCodeSolution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next


if __name__ == "__main__":
    unittest.main()
