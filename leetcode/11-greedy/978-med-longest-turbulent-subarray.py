import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxTurbulenceSize_example1(self):
        self.assertEqual(
            self.solution.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]),
            5,
            "Expected output is 5.",
        )

    def test_maxTurbulenceSize_example2(self):
        self.assertEqual(
            self.solution.maxTurbulenceSize([4, 8, 12, 16]), 2, "Expected output is 2."
        )

    def test_maxTurbulenceSize_example3(self):
        self.assertEqual(
            self.solution.maxTurbulenceSize([100]), 1, "Expected output is 1."
        )

    def test_maxTurbulenceSize_additional(self):
        self.assertEqual(
            self.solution.maxTurbulenceSize([0, 8, 45, 88, 48, 68, 28, 55, 17, 24]),
            8,
            "Expected output is 8.",
        )


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        last = arr[0]
        oper = 0
        res = maxSeq = 1
        for n in arr[1:]:
            if n > last:
                if oper != 2:
                    maxSeq = 2
                else:
                    maxSeq += 1
                oper = 1
            elif n < last:
                if oper != 1:
                    maxSeq = 2
                else:
                    maxSeq += 1
                oper = 2
            else:
                maxSeq = 1
                oper = 1
            last = n
            res = max(res, maxSeq)
        return res


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        sign = False
        b = 0
        res = 1

        # [0, 8, 45, 88, 48, 68, 28, 55, 17, 24]
        for i in range(len(arr)):
            if i == 0:
                continue
            if i - b == 1:
                if arr[i] > arr[i - 1]:
                    sign = True
                elif arr[i] < arr[i - 1]:
                    sign = False
                else:
                    b = i
                continue
            if not (
                (sign and arr[i] < arr[i - 1]) or (not sign and arr[i] > arr[i - 1])
            ):
                res = max(res, i - b)
                b = i - 1
                if arr[i] > arr[i - 1]:
                    sign = True
                elif arr[i] < arr[i - 1]:
                    sign = False
                else:
                    b = i
                continue
            sign = False if sign else True

        return max(res, len(arr) - b)


if __name__ == "__main__":
    unittest.main()
