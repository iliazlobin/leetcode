import unittest
from collections import Counter
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lowest_common_ancestor(self):
        # Test case 1
        root1 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        p1 = TreeNode(5)
        q1 = TreeNode(1)
        self.assertEqual(
            self.solution.lowestCommonAncestor(list_to_tree(root1), p1, q1).val,
            3,
            "Example 1 failed",
        )

        # Test case 2
        root2 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        p2 = TreeNode(5)
        q2 = TreeNode(4)
        self.assertEqual(
            self.solution.lowestCommonAncestor(list_to_tree(root2), p2, q2).val,
            5,
            "Example 2 failed",
        )

        # Test case 3
        root3 = [1, 2]
        p3 = TreeNode(1)
        q3 = TreeNode(2)
        self.assertEqual(
            self.solution.lowestCommonAncestor(list_to_tree(root3), p3, q3).val,
            1,
            "Example 3 failed",
        )

    def test_lowest_common_ancestor_with_last_executed_input(self):
        # Constructing the binary tree from the given input
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)

        # Nodes for which LCA is to be found
        p = TreeNode(5)
        q = TreeNode(1)

        # Solution instance
        solution = Solution()

        # Asserting the LCA
        self.assertEqual(
            solution.lowestCommonAncestor(root, p, q).val,
            3,
            "Failed with last executed input",
        )


# Helper function to convert list to binary tree
def list_to_tree(lst):
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


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(node):
            if not node:
                return None

            if node.val == p.val or node.val == q.val:
                return node

            leftNode = dfs(node.left)
            rightNode = dfs(node.right)
            if leftNode and rightNode:
                return node
            return leftNode or rightNode

        return dfs(root)


if __name__ == "__main__":
    unittest.main()
