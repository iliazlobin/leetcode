import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def test_LRUCache(self):
        lRUCache = LRUCache(2)
        self.assertIsNone(lRUCache.put(1, 1))  # cache is {1=1}
        self.assertIsNone(lRUCache.put(2, 2))  # cache is {1=1, 2=2}
        self.assertEqual(lRUCache.get(1), 1)  # return 1
        self.assertIsNone(
            lRUCache.put(3, 3)
        )  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        self.assertEqual(lRUCache.get(2), -1)  # returns -1 (not found)
        self.assertIsNone(
            lRUCache.put(4, 4)
        )  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        self.assertEqual(lRUCache.get(1), -1)  # return -1 (not found)
        self.assertEqual(lRUCache.get(3), 3)  # return 3
        self.assertEqual(lRUCache.get(4), 4)  # return 4


class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    unittest.main()
