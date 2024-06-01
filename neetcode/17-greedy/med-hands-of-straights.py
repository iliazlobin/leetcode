import heapq
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isNStraightHand(self):
        hand = [1, 2, 4, 2, 3, 5, 3, 4]
        groupSize = 4
        result = self.solution.isNStraightHand(hand, groupSize)
        self.assertTrue(result)

        # hand = [1, 2, 3, 3, 4, 5, 6, 7]
        # groupSize = 4
        # result = self.solution.isNStraightHand(hand, groupSize)
        # self.assertFalse(result)


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        groupNumbers = float(len(hand) / groupSize)
        if not groupNumbers.is_integer():
            return False
        groupNumbers = int(groupNumbers)

        count = {}
        for n in hand:
            count[n] = count.get(n, 0) + 1

        minH = list(count.keys())
        heapq.heapify(minH)
        while hand:
            prev = heapq.heappop(minH)
            for i in range(0, groupNumbers + 1):
                cur = heapq.heappop(minH)
                if prev + 1 != cur:
                    return False
                prev = cur
        return True


if __name__ == "__main__":
    unittest.main()
