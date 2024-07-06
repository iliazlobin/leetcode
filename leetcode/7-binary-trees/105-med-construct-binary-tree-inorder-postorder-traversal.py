from tkinter.tix import Tree
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

    def test_buildTree_postorder_example1(self):
        inorder = [9, 3, 15, 20, 7]
        postorder = [9, 15, 7, 20, 3]
        expected_output = [3, 9, 20, None, None, 15, 7]
        root = self.solution.buildTree(inorder, postorder)
        self.assertEqual(binary_tree_to_list(root), expected_output)

    def test_buildTree_postorder_example2(self):
        inorder = [-1]
        postorder = [-1]
        expected_output = [-1]
        root = self.solution.buildTree(inorder, postorder)
        self.assertEqual(binary_tree_to_list(root), expected_output)


class RSolution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root = TreeNode(postorder.pop())
        idx = inorder.index(root.val)
        root.right = self.buildTree(inorder[idx + 1 :], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)

        return root

class NSolution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = {v: i for i, v in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return None

            root = TreeNode(postorder.pop())
            idx = inorderIdx[root.val]
            root.right = helper(idx + 1, r)
            root.left = helper(l, idx - 1)

            return root

        return helper(0, len(inorder) - 1)


if __name__ == "__main__":
    unittest.main()
