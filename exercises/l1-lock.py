import unittest
from collections import Counter, deque
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def test_getMinCodeEntryTime_case1(self):
        N = 3
        M = 3
        C = [1, 2, 3]
        expected = 2
        result = getMinCodeEntryTime(N, M, C)
        self.assertEqual(expected, result)

    def test_getMinCodeEntryTime_case2(self):
        N = 10
        M = 4
        C = [9, 4, 4, 8]
        expected = 11
        result = getMinCodeEntryTime(N, M, C)
        self.assertEqual(expected, result)


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    res = 0
    cur = 1
    for i in range(M):
        n = C[i]
        if n != cur:
            if n < cur:
                leftDistance = cur - n
                rightDistance = N - cur + n
            elif n > cur:
                leftDistance = cur + N - n
                rightDistance = n - cur
            cur = n
            minDistance = min(leftDistance, rightDistance)
            res += minDistance
    return res


if __name__ == "__main__":
    unittest.main()
