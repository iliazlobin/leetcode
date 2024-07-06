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

    # def test_sumNumbers_example1(self):
    #     root = list_to_binary_tree([1, 2, 3])
    #     expected_output = 25
    #     self.assertEqual(self.solution.sumNumbers(root), expected_output)

    # def test_sumNumbers_example2(self):
    #     root = list_to_binary_tree([4, 9, 0, 5, 1])
    #     expected_output = 1026
    #     self.assertEqual(self.solution.sumNumbers(root), expected_output)

    def test_sumNumbers_example3(self):
        root = list_to_binary_tree([0])
        expected_output = 0
        self.assertEqual(self.solution.sumNumbers(root), expected_output)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        def dfs(node, num):
            nonlocal total

            if not node:
                return

            if not node.left and not node.right:
                if len(num) > 0:
                    total += int(num) * 10 + node.val
                else:
                    total += node.val
                return

            dfs(node.left, num=num + str(node.val))
            dfs(node.right, num + str(node.val))

        dfs(root, "")
        return total


if __name__ == "__main__":
    unittest.main()
