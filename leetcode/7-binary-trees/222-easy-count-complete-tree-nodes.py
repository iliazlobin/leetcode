import unittest
from collections import Counter
from typing import List, Optional

from numpy import count_nonzero


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_binary_tree(lst: List[int]) -> Optional[TreeNode]:
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        node = queue.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root


def binary_tree_to_list(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_countNodes(self):
        # Test case 1
        root1 = list_to_binary_tree([1, 2, 3, 4, 5, 6])
        self.assertEqual(
            self.solution.countNodes(root1),
            6,
            "Failed test case 1: Input: root = [1,2,3,4,5,6] Output: 6",
        )

        # Test case 2
        root2 = list_to_binary_tree([])
        self.assertEqual(
            self.solution.countNodes(root2),
            0,
            "Failed test case 2: Input: root = [] Output: 0",
        )

        # Test case 3
        root3 = list_to_binary_tree([1])
        self.assertEqual(
            self.solution.countNodes(root3),
            1,
            "Failed test case 3: Input: root = [1] Output: 1",
        )


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        leftDepth = 1
        cur = root.left
        while cur:
            cur = cur.left
            leftDepth += 1

        rightDepth = 1
        cur = root.right
        while cur:
            cur = cur.right
            rightDepth += 1

        if leftDepth == rightDepth:
            return pow(2, leftDepth) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


if __name__ == "__main__":
    unittest.main()
