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

    def test_lowestCommonAncestor(self):
        root = list_to_binary_tree([5, 3, 8, 1, 4, 7, 9, None, 2])
        p = TreeNode(3)
        q = TreeNode(8)
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 5)

        root = list_to_binary_tree([5, 3, 8, 1, 4, 7, 9, None, 2])
        p = TreeNode(3)
        q = TreeNode(4)
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 3)


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        while True:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root


if __name__ == "__main__":
    unittest.main()
