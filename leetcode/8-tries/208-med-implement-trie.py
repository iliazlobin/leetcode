import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def test_Trie(self):
        trie = Trie()
        self.assertIsNone(trie.insert("apple"))
        self.assertTrue(trie.search("apple"))  # return True
        self.assertFalse(trie.search("app"))  # return False
        self.assertTrue(trie.startsWith("app"))  # return True
        self.assertIsNone(trie.insert("app"))
        self.assertTrue(trie.search("app"))  # return True


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.node

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.node

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.node

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True


if __name__ == "__main__":
    unittest.main()
