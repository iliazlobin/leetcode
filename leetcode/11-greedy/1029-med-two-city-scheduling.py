import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_twoCitySchedCost_example1(self):
        costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
        expected = 110
        result = self.solution.twoCitySchedCost(costs)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_twoCitySchedCost_example2(self):
        costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
        expected = 1859
        result = self.solution.twoCitySchedCost(costs)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )

    def test_twoCitySchedCost_example3(self):
        costs = [
            [515, 563],
            [451, 713],
            [537, 709],
            [343, 819],
            [855, 779],
            [457, 60],
            [650, 359],
            [631, 42],
        ]
        expected = 3086
        result = self.solution.twoCitySchedCost(costs)
        self.assertEqual(
            expected, result, f"Failed on Example 3 with {result} != {expected}"
        )


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []
        HALF = len(costs) / 2
        # [[10, 20], [30, 200], [400, 50], [30, 20]]
        for c in costs:
            diffs.append((c[0] - c[1], c[0], c[1]))
        diffs = sorted(diffs, key=lambda e: e[0])
        total = 0
        for i in range(len(costs)):
            if i < HALF:
                total += diffs[i][1]
            else:
                total += diffs[i][2]
        return total


class RSolution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = float("inf")
        HALF = len(costs) / 2

        def dfs(i, aCount, bCount, cost):
            nonlocal res

            if i == len(costs):
                res = min(res, cost)
                return

            if aCount < HALF:
                dfs(i + 1, aCount + 1, bCount, cost + costs[i][0])
            if bCount < HALF:
                dfs(i + 1, aCount, bCount + 1, cost + costs[i][1])

        dfs(0, 0, 0, 0)
        return res


if __name__ == "__main__":
    unittest.main()
