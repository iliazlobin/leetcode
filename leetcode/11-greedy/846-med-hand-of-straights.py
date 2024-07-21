import heapq
import unittest
from collections import Counter
from typing import List, Optional

from numpy import sort


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isNStraightHand(self):
        # Example 1
        hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
        groupSize = 3
        self.assertTrue(
            self.solution.isNStraightHand(hand, groupSize), "Failed for Example 1"
        )

        # Example 2
        hand: List[int] = [1, 2, 3, 4, 5]
        groupSize = 4
        self.assertFalse(
            self.solution.isNStraightHand(hand, groupSize), "Failed for Example 2"
        )


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        for c in hand:
            count[c] = count.get(c, 0) + 1

        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for c in range(first, first + groupSize):
                if c not in count:
                    return False
                count[c] -= 1
                if count[c] == 0:
                    heapq.heappop(minH)

        return True


if __name__ == "__main__":
    unittest.main()
