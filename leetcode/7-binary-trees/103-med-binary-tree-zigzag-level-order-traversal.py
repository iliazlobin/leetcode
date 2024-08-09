import unittest
from collections import Counter, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def list_to_binary_tree(self, lst: List[Optional[int]]) -> Optional[TreeNode]:
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

    def binary_tree_to_list(self, root: Optional[TreeNode]) -> List[Optional[int]]:
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
        while result and result[-1] is None:
            result.pop()
        return result


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        oddQ, evenQ = deque(), deque()
        if root:
            oddQ.append(root)
        isOdd = True
        res = []
        while oddQ:
            level = []
            for _ in range(len(oddQ)):
                oddNode = oddQ.popleft()
                if oddNode.left:
                    oddQ.append(oddNode.left)
                if oddNode.right:
                    oddQ.append(oddNode.right)
                evenNode = evenQ.popleft()
                if evenNode.right:
                    evenQ.append(evenNode.right)
                if evenNode.left:
                    evenQ.append(evenNode.left)
                if isOdd:
                    level.append(oddNode.val)
                else:
                    level.append(evenNode.val)
            res.append(level)
            isOdd = False if isOdd else True
        return res


if __name__ == "__main__":
    unittest.main()
