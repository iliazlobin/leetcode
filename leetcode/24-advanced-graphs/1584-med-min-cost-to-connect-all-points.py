import heapq
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minCostConnectPoints(self):
        points1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
        self.assertEqual(
            self.solution.minCostConnectPoints(points1), 20, "Example 1 failed"
        )
        points2 = [[3, 12], [-2, 5], [-4, 1]]
        self.assertEqual(
            self.solution.minCostConnectPoints(points2), 18, "Example 2 failed"
        )


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}  # i : list of [dist, node]

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's
        res = 0
        visit = set()
        minH = [[0, 0]]  # [cost, point]

        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)

            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])

        return res


if __name__ == "__main__":
    unittest.main()
