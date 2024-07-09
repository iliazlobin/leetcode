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


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    return None


if __name__ == "__main__":
    unittest.main()
