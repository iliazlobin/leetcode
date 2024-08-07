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

    def test_diameterOfBinaryTree_example1(self):
        root = list_to_binary_tree([1, 2, 3, 4, 5])
        expected_output = 3
        self.assertEqual(self.solution.diameterOfBinaryTree(root), expected_output)

    def test_diameterOfBinaryTree_example2(self):
        root = list_to_binary_tree([1, 2])
        expected_output = 1
        self.assertEqual(self.solution.diameterOfBinaryTree(root), expected_output)


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            leftLen = dfs(node.left)
            rightLen = dfs(node.right)
            res = max(res, leftLen + rightLen + 1)
            return max(leftLen, rightLen) + 1

        dfs(root)
        return res - 1


if __name__ == "__main__":
    unittest.main()
