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
        self.codec = Codec()

    def test_serialize_and_deserialize(self):
        root = list_to_binary_tree([1, 2, 3, None, None, 4, 5])
        serialized = self.codec.serialize(root)
        deserialized = self.codec.deserialize(serialized)
        self.assertEqual(binary_tree_to_list(deserialized), [1, 2, 3, None, None, 4, 5])

        root = list_to_binary_tree([])
        serialized = self.codec.serialize(root)
        deserialized = self.codec.deserialize(serialized)
        self.assertEqual(binary_tree_to_list(deserialized), [])


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        vals = data.split(",")
        p = 0

        def dfs():
            nonlocal p

            if vals[p] == "N":
                p += 1
                return None
            node = TreeNode(int(vals[p]))
            p += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


if __name__ == "__main__":
    unittest.main()
