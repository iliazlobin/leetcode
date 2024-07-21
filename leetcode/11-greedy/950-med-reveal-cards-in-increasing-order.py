import unittest
from collections import Counter, deque
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_deckRevealedIncreasing_example1(self):
        deck = [17, 13, 11, 2, 3, 5, 7]
        expected = [2, 13, 3, 11, 5, 17, 7]
        result = self.solution.deckRevealedIncreasing(deck)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_deckRevealedIncreasing_example2(self):
        deck = [1, 1000]
        expected = [1, 1000]
        result = self.solution.deckRevealedIncreasing(deck)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)
        res = [0] * len(deck)
        q = deque()
        for i in range(len(deck)):
            q.append(i)
        j = 0
        while q:
            c = deck[j]
            j += 1
            i = q.popleft()
            res[i] = c
            if q:
                s = q.popleft()
                q.append(s)
        return res

if __name__ == "__main__":
    unittest.main()
