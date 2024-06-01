import unittest
from collections import Counter
from typing import List, Optional


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


def list_to_linked_list_with_random(lst):
    if not lst:
        return None

    nodes = [Node(x[0]) for x in lst]
    for i, node in enumerate(nodes):
        if i != len(nodes) - 1:
            node.next = nodes[i + 1]
        if lst[i][1] is not None:
            node.random = nodes[lst[i][1]]
    return nodes[0]


def linked_list_with_random_to_list(node):
    if not node:
        return []

    nodes = []
    while node:
        nodes.append(node)
        node = node.next

    lst = [[node.val, None] for node in nodes]
    for i, node in enumerate(nodes):
        if node.random:
            lst[i][1] = nodes.index(node.random)
    return lst


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        # self.solution = NeetCodeSolution()

    def test_copyRandomList(self):
        # head = list_to_linked_list_with_random(
        #     [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
        # )
        # result = self.solution.copyRandomList(head)
        # self.assertEqual(
        #     linked_list_with_random_to_list(result),
        #     [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        # )

        # head = list_to_linked_list_with_random([[1, 1], [2, 1]])
        # result = self.solution.copyRandomList(head)
        # self.assertEqual(linked_list_with_random_to_list(result), [[1, 1], [2, 1]])

        head = list_to_linked_list_with_random([[3, None], [3, 0], [3, None]])
        result = self.solution.copyRandomList(head)
        self.assertEqual(
            linked_list_with_random_to_list(result), [[3, None], [3, 0], [3, None]]
        )


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        oldToCopy = {None: None}

        cur = head
        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]


class NeetCodeSolution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]


if __name__ == "__main__":
    unittest.main()
