import unittest
from collections import Counter
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def list_to_binary_tree(self, lst: List[Optional[int]]) -> Optional[TreeNode]:
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

    def binary_tree_to_list(self, root: Optional[TreeNode]) -> List[Optional[int]]:
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

    def test_minDiffInBST_example1(self):
        root = self.list_to_binary_tree([4, 2, 6, 1, 3])
        expected = 1
        result = self.solution.minDiffInBST(root)
        self.assertEqual(result, expected)

    def test_minDiffInBST_example2(self):
        root = self.list_to_binary_tree([1, 0, 48, None, None, 12, 49])
        expected = 1
        result = self.solution.minDiffInBST(root)
        self.assertEqual(result, expected)


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = float("inf")
        prev = None

        def dfs(node):
            nonlocal res, prev

            if not node:
                return

            dfs(node.left)
            if prev != None:
                res = min(res, node.val - prev)
            prev = node.val
            dfs(node.right)

        dfs(root)
        return res


if __name__ == "__main__":
    unittest.main()
