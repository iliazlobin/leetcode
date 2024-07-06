import unittest
from collections import Counter
from typing import List, Optional

from sympy import N


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
    def test_BSTIterator(self):
        root = list_to_binary_tree([7, 3, 15, None, None, 9, 20])
        bstIterator = BSTIterator(root)
        # self.assertIsNone(
        #     bstIterator.next(), "First call to next should return 3 but got None"
        # )
        self.assertEqual(bstIterator.next(), 3, "Expected next to return 3")
        self.assertEqual(bstIterator.next(), 7, "Expected next to return 7")
        self.assertTrue(bstIterator.hasNext(), "Expected hasNext to return True")
        self.assertEqual(bstIterator.next(), 9, "Expected next to return 9")
        self.assertTrue(bstIterator.hasNext(), "Expected hasNext to return True")
        self.assertEqual(bstIterator.next(), 15, "Expected next to return 15")
        self.assertTrue(bstIterator.hasNext(), "Expected hasNext to return True")
        self.assertEqual(bstIterator.next(), 20, "Expected next to return 20")
        self.assertFalse(bstIterator.hasNext(), "Expected hasNext to return False")

    def test_BSTIterator_sequence(self):
        root = list_to_binary_tree([3, 1, 4, None, 2])
        bstIterator = BSTIterator(root)
        self.assertTrue(bstIterator.hasNext(), "Expected hasNext to return True")
        self.assertEqual(bstIterator.next(), 1, "Expected next to return 1")
        self.assertTrue(bstIterator.hasNext(), "Expected hasNext to return True")
        self.assertEqual(bstIterator.next(), 2, "Expected next to return 2")
        self.assertTrue(bstIterator.hasNext(), "Expected hasNext to return True")
        self.assertEqual(bstIterator.next(), 3, "Expected next to return 3")
        self.assertTrue(bstIterator.hasNext(), "Expected hasNext to return True")
        self.assertEqual(bstIterator.next(), 4, "Expected next to return 4")
        self.assertFalse(bstIterator.hasNext(), "Expected hasNext to return False")


class BSTIterator:
    stack = []

    def __init__(self, root: Optional[TreeNode]):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        res = self.stack.pop()
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


if __name__ == "__main__":
    unittest.main()
