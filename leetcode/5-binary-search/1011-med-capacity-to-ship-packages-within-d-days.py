import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_shipWithinDays_example1(self):
        weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        days = 5
        expected_output = 15
        self.assertEqual(self.solution.shipWithinDays(weights, days), expected_output)

    def test_shipWithinDays_example2(self):
        weights = [3, 2, 2, 4, 1, 4]
        days = 3
        expected_output = 6
        self.assertEqual(self.solution.shipWithinDays(weights, days), expected_output)

    def test_shipWithinDays_example3(self):
        weights = [1, 2, 3, 1, 1]
        days = 4
        expected_output = 3
        self.assertEqual(self.solution.shipWithinDays(weights, days), expected_output)


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r = sum(weights)
        l = max(weights)
        while l <= r:
            m = (l + r) // 2
            cap = 0
            ships = 1
            for w in weights:
                if cap + w <= m:
                    cap += w
                else:
                    cap = w
                    ships += 1
            if ships > days:
                l = m + 1
            else:
                r = m - 1
        return l



if __name__ == "__main__":
    unittest.main()
