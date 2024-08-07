import unittest
from collections import Counter, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def binary_tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
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
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result

    def list_to_binary_tree(self, lst):
        if not lst:
            return None
        root = TreeNode(lst[0])
        queue = [root]
        i = 1
        while queue and i < len(lst):
            node = queue.pop(0)
            if i < len(lst) and lst[i] is not None:
                node.left = TreeNode(lst[i])
                queue.append(node.left)
            i += 1
            if i < len(lst) and lst[i] is not None:
                node.right = TreeNode(lst[i])
                queue.append(node.right)
            i += 1
        return root

    def test_leafSimilar_example1(self):
        root1 = self.list_to_binary_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
        root2 = self.list_to_binary_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    # def test_leafSimilar_example2(self):
    #     root1 = self.list_to_binary_tree([1, 2, 3])
    #     root2 = self.list_to_binary_tree([1, 3, 2])
    #     self.assertFalse(self.solution.leafSimilar(root1, root2))


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, leaf):
            if not node:
                return
            if not node.left and not node.right:
                leaf.append(node.val)
                return
            dfs(node.left, leaf)
            dfs(node.right, leaf)
        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        return leaf1 == leaf2


if __name__ == "__main__":
    unittest.main()
