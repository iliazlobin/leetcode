import unittest
from collections import Counter, deque
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def test_getMinProblemCount_case1(self):
        N = 6
        S = [1, 2, 3, 4, 5, 6]
        expected = 4
        result = getMinProblemCount(N, S)
        self.assertEqual(expected, result)

    def test_getMinProblemCount_case2(self):
        N = 4
        S = [4, 3, 3, 4]
        expected = 3
        result = getMinProblemCount(N, S)
        self.assertEqual(expected, result)

    def test_getMinProblemCount_case3(self):
        N = 4
        S = [2, 4, 6, 8]
        expected = 4
        result = getMinProblemCount(N, S)
        self.assertEqual(expected, result)


def getMinProblemCount(N: int, S: List[int]) -> int:
    largest = max(S)
    half = int(largest / 2)
    if largest % 2:
        return half + 1
    for i in range(len(S)):
        n = S[i]
        if n % 2:
            return half + 1
    return half


if __name__ == "__main__":
    unittest.main()
