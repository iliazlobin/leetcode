import unittest
from collections import Counter, deque
from typing import List, Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def list_to_tree_with_next(self, lst):
    # Helper function to convert list to tree with next pointers
    if not lst:
        return None
    root = Node(lst[0])
    queue = deque([root])
    i = 1
    while queue and i < len(lst):
        current = queue.popleft()
        if lst[i] is not None:
            current.left = Node(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = Node(lst[i])
            queue.append(current.right)
        i += 1
    return root


def tree_to_list_with_next(self, root):
    # Helper function to convert tree with next pointers to list
    if not root:
        return []
    result = []
    level = [root]
    while level:
        next_level = []
        for node in level:
            result.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        result.append("#")  # Mark the end of the current level
        level = next_level
    return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_connect_example1(self):
        root = list_to_tree_with_next([1, 2, 3, 4, 5, None, 7])
        connected_root = self.solution.connect(root)
        self.assertEqual(
            self.tree_to_list_with_next(connected_root),
            [1, "#", 2, 3, "#", 4, 5, 7, "#"],
        )

    # def test_connect_example2(self):
    #     root = list_to_tree_with_next([])
    #     connected_root = self.solution.connect(root)
    #     self.assertEqual(self.tree_to_list_with_next(connected_root), [])


class Solution:
    def connect(self, root: "Node") -> "Node":
        queue = deque()
        queue.append(root)
        nextQueue = deque()
        while queue:
            node = queue.popleft()
            if not node:
                continue
            node.next = queue[0] if queue else None

            if node.left:
                nextQueue.append(node.left)
            if node.right:
                nextQueue.append(node.right)

            if not queue:
                queue = nextQueue
                nextQueue = deque()

        return root



class NSolution:
    def connect(self, root: "Node") -> "Node":
        cur, nxt = root, root.left if root else None

        while cur and nxt:
            cur.left.next = nxt.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left

        return root


class RSolution:
    def connect(self, root: "Node") -> "Node":
        hashM = {}

        def dfs(node, level):
            if not node:
                hashM[level] = None
                return None

            if level not in hashM:
                hashM[level] = node
                node.next = None
            else:
                node.next = hashM[level]

            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return root


if __name__ == "__main__":
    unittest.main()
