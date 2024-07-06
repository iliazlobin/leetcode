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

    def test_isSameTree_example1(self):
        p = list_to_binary_tree([1, 2, 3])
        q = list_to_binary_tree([1, 2, 3])
        self.assertTrue(self.solution.isSameTree(p, q))

    def test_isSameTree_example2(self):
        p = list_to_binary_tree([1, 2])
        q = list_to_binary_tree([1, None, 2])
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_isSameTree_example3(self):
        p = list_to_binary_tree([1, 2, 1])
        q = list_to_binary_tree([1, 1, 2])
        self.assertFalse(self.solution.isSameTree(p, q))


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)

        return dfs(p, q)


if __name__ == "__main__":
    unittest.main()
