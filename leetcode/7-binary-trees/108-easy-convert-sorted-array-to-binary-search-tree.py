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


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
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

    def test_sortedArrayToBST_empty(self):
        nums = []
        expected = []
        result = self.solution.sortedArrayToBST(nums)
        self.assertEqual(tree_to_list(result), expected)

    def test_sortedArrayToBST_single_element(self):
        nums = [1]
        expected = [1]
        result = self.solution.sortedArrayToBST(nums)
        self.assertEqual(tree_to_list(result), expected)

    def test_sortedArrayToBST_multiple_elements(self):
        nums = [1, 2, 3]
        expected = [2, 1, 3]
        result = self.solution.sortedArrayToBST(nums)
        self.assertEqual(tree_to_list(result), expected)

    def test_sortedArrayToBST_larger_array(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        expected = [4, 2, 6, 1, 3, 5, 7]
        result = self.solution.sortedArrayToBST(nums)
        self.assertEqual(tree_to_list(result), expected)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = build(l, m - 1)
            root.right = build(m + 1, r)
            return root

        return build(0, len(nums) - 1)


if __name__ == "__main__":
    unittest.main()
