import unittest
from collections import Counter, deque
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def test_getMaximumEatenDishCount_case1(self):
        N = 6
        D = [1, 2, 3, 3, 2, 1]
        K = 1
        expected = 5
        result = getMaximumEatenDishCount(N, D, K)
        self.assertEqual(expected, result)

    def test_getMaximumEatenDishCount_case2(self):
        N = 6
        D = [1, 2, 3, 3, 2, 1]
        K = 2
        expected = 4
        result = getMaximumEatenDishCount(N, D, K)
        self.assertEqual(expected, result)

    def test_getMaximumEatenDishCount_case3(self):
        N = 7
        D = [1, 2, 1, 2, 1, 2, 1]
        K = 2
        expected = 2
        result = getMaximumEatenDishCount(N, D, K)
        self.assertEqual(expected, result)


def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    res = 0
    consumed = {}
    queue = deque()

    for right in range(N):
        curr = D[right]
        if curr not in consumed:
            consumed[curr] = True
            res += 1
            queue.append(curr)

        if len(queue) > K:
            oldDish = queue.popleft()
            del consumed[oldDish]

    return res


if __name__ == "__main__":
    unittest.main()
