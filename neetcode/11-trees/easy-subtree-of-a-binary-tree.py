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

    def test_isSubtree(self):
        root = list_to_binary_tree([1, 2, 3, 4, 5])
        subRoot = list_to_binary_tree([2, 4, 5])
        result = self.solution.isSubtree(root, subRoot)
        self.assertEqual(result, True)

        root = list_to_binary_tree([1, 2, 3, 4, 5, None, None, 6])
        subRoot = list_to_binary_tree([2, 4, 5])
        result = self.solution.isSubtree(root, subRoot)
        self.assertEqual(result, False)


class Solution:
    def isEquivalent(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not (p and q and p.val == q.val):
            return False
        return self.isEquivalent(p.left, q.left) and self.isEquivalent(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isEquivalent(root, subRoot):
            return True
        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        return False


if __name__ == "__main__":
    unittest.main()
