import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_successfulPairs_example1(self):
        spells = [5, 1, 3]
        potions = [1, 2, 3, 4, 5]
        success = 7
        expected_output = [4, 0, 3]
        self.assertEqual(
            self.solution.successfulPairs(spells, potions, success), expected_output
        )

    def test_successfulPairs_example2(self):
        spells = [3, 1, 2]
        potions = [8, 5, 8]
        success = 16
        expected_output = [2, 0, 2]
        self.assertEqual(
            self.solution.successfulPairs(spells, potions, success), expected_output
        )


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        res = [0] * len(spells)
        for i, s in enumerate(spells):
            l, r = 0, len(potions) - 1
            while l <= r:
                m = (l + r) // 2
                cost = s * potions[m]
                if cost < success:
                    l = m + 1
                else:
                    r = m - 1
            res[i] = len(potions) - l
        return res


if __name__ == "__main__":
    unittest.main()
