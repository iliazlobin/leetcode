import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findWords(self):
        # board = [
        #     ["o", "a", "a", "n"],
        #     ["e", "t", "a", "e"],
        #     ["i", "h", "k", "r"],
        #     ["i", "f", "l", "v"],
        # ]
        # words = ["oath", "pea", "eat", "rain"]
        # self.assertCountEqual(self.solution.findWords(board, words), ["eat", "oath"])

        # board = [["a", "b"], ["c", "d"]]
        # words = ["abcb"]
        # self.assertCountEqual(self.solution.findWords(board, words), [])

        board = [
            ["a", "b", "c", "d"],
            ["s", "a", "a", "t"],
            ["a", "c", "k", "e"],
            ["a", "c", "d", "n"],
        ]
        words = ["bat", "cat", "back", "backend", "stack"]
        self.assertCountEqual(
            self.solution.findWords(board, words), ["back", "backend", "cat"]
        )


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, s):
        cur = self
        for c in s:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for w in words:
            trie.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or (r, c) in visit
                or board[r][c] not in node.children
            ):
                return False

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)

            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie, "")

        return res


if __name__ == "__main__":
    unittest.main()
