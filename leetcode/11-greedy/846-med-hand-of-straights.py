import heapq
import unittest
from collections import Counter
from typing import List, Optional


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


# O(logN*N)
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        for n in hand:
            count[n] = count.get(n, 0) + 1

        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1

                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)

        return True


if __name__ == "__main__":
    unittest.main()
