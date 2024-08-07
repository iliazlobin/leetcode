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

    def test_rangeSumBST_example1(self):
        root = self.list_to_binary_tree([10, 5, 15, 3, 7, None, 18])
        low = 7
        high = 15
        expected = 32
        result = self.solution.rangeSumBST(root, low, high)
        self.assertEqual(result, expected)

    def test_rangeSumBST_example2(self):
        root = self.list_to_binary_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        low = 6
        high = 10
        expected = 23
        result = self.solution.rangeSumBST(root, low, high)
        self.assertEqual(result, expected)


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return
            if low <= node.val <= high:
                res += node.val
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)

        dfs(root)
        return res


if __name__ == "__main__":
    unittest.main()
