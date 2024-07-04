import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_canCompleteCircuit(self):
        # Example 1
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        self.assertEqual(
            self.solution.canCompleteCircuit(gas, cost), 3, "Failed for Example 1"
        )

        # Example 2
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        self.assertEqual(
            self.solution.canCompleteCircuit(gas, cost), -1, "Failed for Example 2"
        )

        gas = [5, 1, 2, 3, 4]
        cost = [4, 4, 1, 5, 1]
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), 4, "Failed for custom case")

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        diffs = [0] * len(gas)
        for i in range(len(gas)):
            diffs[i] = gas[i] - cost[i]

        start = 0
        total = 0
        for i in range(len(diffs)):
            if total + diffs[i] < 0:
                start = i + 1 if start < len(diffs) else 0
                total = 0
            else:
                total += diffs[i]

        return start


if __name__ == "__main__":
    unittest.main()
