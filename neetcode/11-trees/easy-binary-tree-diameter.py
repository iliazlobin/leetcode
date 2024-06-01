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
        # self.solution = NeetCodeSolution()

    def test_diameterOfBinaryTree(self):
        root = list_to_binary_tree([1, None, 2, 3, 4, 5])
        result = self.solution.diameterOfBinaryTree(root)
        self.assertEqual(result, 3)

        root = list_to_binary_tree([1, 2, 3])
        result = self.solution.diameterOfBinaryTree(root)
        self.assertEqual(result, 2)


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def calculateDiameter(root: Optional[TreeNode]) -> int:
            nonlocal maxDiameter

            if not root:
                return 0

            leftDiameter = calculateDiameter(root.left)
            rightDiameter = calculateDiameter(root.right)
            diameter = leftDiameter + rightDiameter
            maxDiameter = max(maxDiameter, diameter)
            return max(leftDiameter, rightDiameter) + 1

        calculateDiameter(root)
        return maxDiameter


class NeetCodeSolution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res


if __name__ == "__main__":
    unittest.main()
