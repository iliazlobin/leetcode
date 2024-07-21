import unittest
from collections import Counter, deque
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_predictPartyVictory_example1(self):
        self.assertEqual(
            self.solution.predictPartyVictory("RD"), "Radiant", "Example 1 failed."
        )

    def test_predictPartyVictory_example2(self):
        self.assertEqual(
            self.solution.predictPartyVictory("RDD"), "Dire", "Example 2 failed."
        )


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQueue, dQueue = deque(), deque()

        for i, c in enumerate(senate):
            if c == "R":
                rQueue.append(i)
            else:
                dQueue.append(i)

        offset = len(senate)
        while rQueue and dQueue:
            r = rQueue.popleft()
            d = dQueue.popleft()
            if r < d:
                rQueue.append(offset + r)
            else:
                dQueue.append(offset + d)

        return "Radiant" if rQueue else "Dire"


if __name__ == "__main__":
    unittest.main()
