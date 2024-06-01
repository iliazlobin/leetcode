import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_exist(self):
        board = [["A", "B", "C", "D"], ["S", "A", "A", "T"], ["A", "C", "A", "E"]]
        word = "CAT"
        result = self.solution.exist(board, word)
        self.assertEqual(result, True)

        board = [["A", "B", "C", "D"], ["S", "A", "A", "T"], ["A", "C", "A", "E"]]
        word = "BAT"
        result = self.solution.exist(board, word)
        self.assertEqual(result, False)

        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCB"
        result = self.solution.exist(board, word)
        self.assertEqual(result, False)

        board = [["a"]]
        word = "a"
        result = self.solution.exist(board, word)
        self.assertEqual(result, True)


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r, c, w):
            if w == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or word[w] != board[r][c]:
                return False

            visit.add((r, c))
            if (
                dfs(r - 1, c, w + 1)
                or dfs(r, c - 1, w + 1)
                or dfs(r + 1, c, w + 1)
                or dfs(r, c + 1, w + 1)
            ):
                return True
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


if __name__ == "__main__":
    unittest.main()
