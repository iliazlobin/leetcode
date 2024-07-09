import unittest
from collections import Counter
from typing import List, Optional


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

    # def test_example1(self):
    #     root = TreeNode(4)
    #     root.left = TreeNode(2)
    #     root.left.left = TreeNode(1)
    #     root.left.right = TreeNode(3)
    #     root.right = TreeNode(6)
    #     self.assertEqual(self.solution.getMinimumDifference(root), 1)

    # def test_example2(self):
    #     root = TreeNode(1)
    #     root.left = TreeNode(0)
    #     root.right = TreeNode(48)
    #     root.right.left = TreeNode(12)
    #     root.right.right = TreeNode(49)
    #     self.assertEqual(self.solution.getMinimumDifference(root), 1)

    def test_custom(self):
        root = TreeNode(0)
        root.right = TreeNode(2236)
        root.right.left = TreeNode(1277)
        root.right.right = TreeNode(2776)
        root.right.left.left = TreeNode(519)
        self.assertEqual(self.solution.getMinimumDifference(root), 519)


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev, res = None, float("inf")

        def dfs(node):
            nonlocal res, prev

            if not node:
                return

            dfs(node.left)

            if prev is not None:
                res = min(res, node.val - prev)
            prev = node.val

            dfs(node.right)

        dfs(root)
        return res


if __name__ == "__main__":
    unittest.main()
