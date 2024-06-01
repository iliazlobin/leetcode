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

    def test_goodNodes(self):
        # root = list_to_binary_tree([2, 1, 1, 3, None, 1, 5])
        # result = self.solution.goodNodes(root)
        # self.assertEqual(result, 3)

        # root = list_to_binary_tree([1, 2, -1, 3, 4])
        # result = self.solution.goodNodes(root)
        # self.assertEqual(result, 4)

        # root = list_to_binary_tree([3, 1, 4, 3, None, 1, 5])
        # result = self.solution.goodNodes(root)
        # self.assertEqual(result, 4)

        root = list_to_binary_tree([-1,5,-2,4,4,2,-2,None,None,-4,None,-2,3,None,-2,0,None,-1,None,-3,None,-4,-3,3,None,None,None,None,None,None,None,3,-3])
        result = self.solution.goodNodes(root)
        self.assertEqual(result, 5)


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(maxVal, node: TreeNode):
            nonlocal res

            if not node:
                return
            if node.val >= maxVal:
                res += 1
            maxVal = max(maxVal, node.val)
            dfs(maxVal, node.left)
            dfs(maxVal, node.right)

        dfs(root.val, root)
        return res


class NeetCodeSolution:
    def goodNodes(self, root: TreeNode) -> int:
        values = []
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            values.append(res)
            return res

        r = dfs(root, root.val)
        return r

if __name__ == "__main__":
    unittest.main()
