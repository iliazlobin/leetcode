import heapq
import unittest
from collections import Counter, deque
from typing import List, Optional

from sklearn.base import defaultdict


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_networkDelayTime(self):
        times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n1 = 4
        k1 = 2
        self.assertEqual(
            self.solution.networkDelayTime(times1, n1, k1), 2, "Example 1 failed"
        )
        times2 = [[1, 2, 1]]
        n2 = 2
        k2 = 1
        self.assertEqual(
            self.solution.networkDelayTime(times2, n2, k2), 1, "Example 2 failed"
        )
        times = [[1, 2, 1]]
        n = 2
        k = 2
        self.assertEqual(
            self.solution.networkDelayTime(times, n, k), -1, "Test with k=2 failed"
        )
        times = [[1, 2, 1], [2, 3, 2], [1, 3, 4]]
        n = 3
        k = 1
        self.assertEqual(
            self.solution.networkDelayTime(times, n, k),
            3,
            "Additional case with times=[[1,2,1],[2,3,2],[1,3,4]], n=3, k=1 failed",
        )

class Solution:
    def networkDelayTime(self, times: List[List[int]], n1: int, k: int) -> int:
        edges = defaultdict(list)

        for u, n2, w1 in times:
            edges[u].append((n2, w1))

        minHeap = [(0, k)]
        visit = set()
        res = 0

        while minHeap:
            w1, n = heapq.heappop(minHeap)
            if n in visit:
                continue
            visit.add(n)
            res = max(res, w1)
            for n2, w2 in edges[n]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return res if len(visit) == n1 else -1


class FSolution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(n + 1)}

        for t in times:
            adj[t[0]].append([t[1], t[2]])

        nodeLatency = {}
        nodeLatency[k] = 0
        queue = deque()
        queue.append([k, 0])  # node, elapsed
        maxTime = 0

        while queue:
            cur, elapsed = queue.popleft()
            for node, latency in adj[cur]:
                time = elapsed + latency

                if node in nodeLatency and maxTime == nodeLatency[node]:
                    maxTime = time
                else:
                    maxTime = max(maxTime, time)

                if node not in nodeLatency or (
                    node in nodeLatency and time < nodeLatency[node]
                ):
                    nodeLatency[node] = time

                queue.append([node, time])

        return maxTime if len(nodeLatency) == n else -1


if __name__ == "__main__":
    unittest.main()
