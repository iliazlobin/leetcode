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

    def test_isBalanced(self):
        root = list_to_binary_tree([1, 2, 3, None, None, 4])
        result = self.solution.isBalanced(root)
        self.assertEqual(result, True)

        root = list_to_binary_tree([1, 2, 3, None, None, 4, None, 5])
        result = self.solution.isBalanced(root)
        self.assertEqual(result, False)

        root = list_to_binary_tree([])
        result = self.solution.isBalanced(root)
        self.assertEqual(result, True)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def treeHight(root: Optional[TreeNode]):
            if not root:
                return (0, False)
            leftHight = treeHight(root.left)
            rightHight = treeHight(root.right)
            if leftHight[1] or rightHight[1]:
                return (0, True)
            if abs(leftHight[0] - rightHight[0]) > 1:
                return (0, True)
            maxHight = max(leftHight[0], rightHight[0])
            return (maxHight + 1, False)

        res = treeHight(root)
        return not res[1]


if __name__ == "__main__":
    unittest.main()
