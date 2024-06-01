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

    def test_findDuplicate(self):
        nums = [1, 3, 4, 2, 2]
        result = self.solution.findDuplicate(nums)
        self.assertEqual(result, 2)

        nums = [3, 1, 3, 4, 2]
        result = self.solution.findDuplicate(nums)
        self.assertEqual(result, 3)

        nums = [3, 3, 3, 3, 3]
        result = self.solution.findDuplicate(nums)
        self.assertEqual(result, 3)


class OnSolution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        prev = nums[0]
        for n in nums[1:]:
            if prev == n:
                return n
            prev = n
        return -1


class OxSolution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = {}
        for i, n in enumerate(nums):
            map[i] = ListNode(n)
        for i, n in enumerate(nums):
            map[i].next = map[n]
        start = map[0]

        slow, fast = start.next, start.next.next
        while slow.val != fast.val:
            slow = slow.next
            fast = fast.next.next

        slow2 = start
        while slow.val != slow2.val:
            slow = slow.next
            slow2 = slow2.next

        return slow2.val

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break

        return slow2

if __name__ == "__main__":
    unittest.main()
