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

    def test_hasPathSum_example1(self):
        root = list_to_binary_tree(
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
        )
        targetSum = 22
        self.assertTrue(self.solution.hasPathSum(root, targetSum))

    def test_hasPathSum_example2(self):
        root = list_to_binary_tree([1, 2, 3])
        targetSum = 5
        self.assertFalse(self.solution.hasPathSum(root, targetSum))

    def test_hasPathSum_example3(self):
        root = list_to_binary_tree([])
        targetSum = 0
        self.assertFalse(self.solution.hasPathSum(root, targetSum))

    def test_hasPathSum_new_example(self):
        root = list_to_binary_tree([1, 2])
        targetSum = 1
        self.assertFalse(self.solution.hasPathSum(root, targetSum))


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, total):
            if node is None:
                return False

            if not node.left and not node.right:
                if total + node.val == targetSum:
                    return True
                else:
                    return False

            if dfs(node.left, total + node.val) or dfs(node.right, total + node.val):
                return True
            return False

        if not root:
            return False
        return dfs(root, 0)


class LSolution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        if targetSum - root.val == 0 and not root.right and not root.left:
            return True
        return self.hasPathSum(root.right, targetSum - root.val) or self.hasPathSum(
            root.left, targetSum - root.val
        )


if __name__ == "__main__":
    unittest.main()
