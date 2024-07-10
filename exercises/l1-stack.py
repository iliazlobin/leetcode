import unittest
from collections import Counter, deque
from typing import List, Optional


class TestStabilizeDiscStack(unittest.TestCase):
    def test_stabilize_disc_stack_case1(self):
        N = 5
        R = [2, 5, 3, 6, 5]
        expected = 3
        result = getMinimumDeflatedDiscCount(N, R)
        self.assertEqual(expected, result)

    def test_stabilize_disc_stack_case2(self):
        N = 3
        R = [100, 100, 100]
        expected = 2
        result = getMinimumDeflatedDiscCount(N, R)
        self.assertEqual(expected, result)

    def test_stabilize_disc_stack_case3(self):
        N = 4
        R = [6, 5, 4, 3]
        expected = -1
        result = getMinimumDeflatedDiscCount(N, R)
        self.assertEqual(expected, result)


def getMinimumDeflatedDiscCount(N, R):
    minRad = float("inf")
    count = 0

    for i in range(N - 1, -1, -1):
        if R[i] >= minRad:
            if minRad == 1:
                return -1
            count += 1
            R[i] = minRad - 1

        minRad = R[i]

    return count


if __name__ == "__main__":
    unittest.main()
