import unittest
from collections import Counter
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

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

    def test_mergeTrees_example1(self):
        root1 = self.list_to_binary_tree([1, 3, 2, 5])
        root2 = self.list_to_binary_tree([2, 1, 3, None, 4, None, 7])
        expected = [3, 4, 5, 5, 4, None, 7]
        result = self.solution.mergeTrees(root1, root2)
        self.assertEqual(binary_tree_to_list(result), expected)

    def test_mergeTrees_example2(self):
        root1 = self.list_to_binary_tree([1])
        root2 = self.list_to_binary_tree([1, 2])
        expected = [2, 2]
        result = self.solution.mergeTrees(root1, root2)
        self.assertEqual(binary_tree_to_list(result), expected)


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        def dfs(node1, node2):
            if not node1 and not node2:
                return None
            node = None
            if node1 and node2:
                node = TreeNode(node1.val + node2.val)
                node.left = dfs(node1.left, node2.left)
                node.right = dfs(node1.right, node2.right)
            elif node1:
                node = node1
            else:
                node = node2
            return node

        return dfs(root1, root2)


if __name__ == "__main__":
    unittest.main()
