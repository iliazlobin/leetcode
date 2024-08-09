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

    def test_rightSideView_example1(self):
        root = self.list_to_binary_tree([1, 2, 3, None, 5, None, 4])
        expected = [1, 3, 4]
        result = self.solution.rightSideView(root)
        self.assertEqual(result, expected)

    def test_rightSideView_example2(self):
        root = self.list_to_binary_tree([1, None, 3])
        expected = [1, 3]
        result = self.solution.rightSideView(root)
        self.assertEqual(result, expected)

    def test_rightSideView_example3(self):
        root = self.list_to_binary_tree([])
        expected = []
        result = self.solution.rightSideView(root)
        self.assertEqual(result, expected)


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        if root:
            q.append(root)
        while q:
            n = deque()
            if q[0]:
                res.append(q[0].val)
            while q:
                node = q.popleft()
                if node.right:
                    n.append(node.right)
                if node.left:
                    n.append(node.left)
            q = n
        return res


if __name__ == "__main__":
    unittest.main()
