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

    def test_levelOrder_example1(self):
        root = self.list_to_binary_tree([3, 9, 20, None, None, 15, 7])
        expected = [[3], [9, 20], [15, 7]]
        result = self.solution.levelOrder(root)
        self.assertEqual(result, expected)

    def test_levelOrder_example2(self):
        root = self.list_to_binary_tree([1])
        expected = [[1]]
        result = self.solution.levelOrder(root)
        self.assertEqual(result, expected)

    def test_levelOrder_example3(self):
        root = self.list_to_binary_tree([])
        expected = []
        result = self.solution.levelOrder(root)
        self.assertEqual(result, expected)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        if root:
            q.append(root)
        while q:
            n = deque()
            level = []
            while q:
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    n.append(node.left)
                if node.right:
                    n.append(node.right)
            res.append(level)
            q = n
        return res


if __name__ == "__main__":
    unittest.main()
