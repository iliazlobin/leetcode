import unittest
from collections import Counter, deque
from typing import List, Optional


class TestSolution(unittest.TestCase):
    # def test_getMinProblemCount_case1(self):
    #     N = 1
    #     S = [1]
    #     expected = 1
    #     result = getMinProblemCount(N, S)
    #     self.assertEqual(expected, result)

    # def test_getMinProblemCount_case2(self):
    #     N = 1
    #     S = [1000000000]
    #     expected = 333333334
    #     result = getMinProblemCount(N, S)
    #     self.assertEqual(expected, result)

    # def test_getMinProblemCount_case3(self):
    #     N = 3
    #     S = [1, 2, 3]
    #     expected = 3
    #     result = getMinProblemCount(N, S)
    #     self.assertEqual(expected, result)

    # def test_getMinProblemCount_case4(self):
    #     N = 2
    #     S = [4, 5]
    #     expected = 3
    #     result = getMinProblemCount(N, S)
    #     self.assertEqual(expected, result)

    # def test_getMinProblemCount_case5(self):
    #     N = 5
    #     S = [6, 9, 12, 15, 18]
    #     expected = 6
    #     result = getMinProblemCount(N, S)
    #     self.assertEqual(expected, result)

    # def test_getMinProblemCount_case6(self):
    #     N = 2
    #     S = [1, 6]
    #     expected = 6
    #     result = getMinProblemCount(N, S)
    #     self.assertEqual(expected, result)

    # def test_getMinProblemCount_case7(self):
    #     N = 5
    #     S = [2, 4, 6, 8, 10]
    #     expected = 5
    #     result = getMinProblemCount(N, S)
    #     self.assertEqual(expected, result)

    def test_getMinProblemCount_case8(self):
        N = 3
        S = [2, 5, 8] # [3, 3, 2]
        expected = 3
        result = getMinProblemCount(N, S)
        self.assertEqual(expected, result)

    # def test_getMinProblemCount_case9(self):
    #     N = 4
    #     S = [3, 6, 9, 12]
    #     expected = 4
    #     result = getMinProblemCount(N, S)
    #     self.assertEqual(expected, result)

    # def test_getMinProblemCount_case10(self):
    #     N = 5
    #     S = [3, 5, 8, 10, 15]
    #     expected = 5
    #     result = getMinProblemCount(N, S)
    #     self.assertEqual(expected, result)

def getMinProblemCount(N: int, S: List[int]) -> int:
    isOne = 0
    isTwo = 0
    threes = 0
    for i in range(N):
        n = S[i]
        threes = max(threes, n // 3)
        r = n % 3
        if not isOne and r == 1:
            isOne = 1
        if not isTwo and r == 2:
            isTwo = 1
    return threes + isOne + isTwo


if __name__ == "__main__":
    unittest.main()
