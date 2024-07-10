from ossaudiodev import control_names
import unittest
from collections import Counter, deque
from typing import List, Optional


class TestGetMaxAdditionalDinersCount(unittest.TestCase):
    def test_case1(self):
        N = 10
        K = 1
        M = 2
        S = [2, 6]
        expected = 3
        result = getMaxAdditionalDinersCount(N, K, M, S)
        self.assertEqual(expected, result)

    def test_case2(self):
        N = 15
        K = 2
        M = 3
        S = [11, 6, 14]
        expected = 1
        result = getMaxAdditionalDinersCount(N, K, M, S)
        self.assertEqual(expected, result)


def getMaxAdditionalDinersCount(N, K, M, S):
    S.sort()

    counter = 0

    if S[0] > 1:
        counter += (S[0] - 1) // (K + 1)

    for i in range(1, M):
        gap = S[i] - S[i - 1] - 1
        if gap > K:
            counter += (gap - K) // (K + 1)

    if S[-1] < N:
        counter += (N - S[-1]) // (K + 1)

    return counter


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    seats = [False] * N

    for s in S:
        for i in range(max(0, s - K - 1), min(s + K, N)):
            seats[i] = True

    count = 0
    for i, s in enumerate(seats):
        if s:
            continue
        count += 1
        for k in range(i, min(i + K + 1, N)):
            seats[k] = True

    return count


def getMaxAdditionalDinersCount2(N: int, M: int, C: List[int]) -> int:
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
