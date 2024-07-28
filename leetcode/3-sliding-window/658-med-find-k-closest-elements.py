import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findClosestElements_example1(self):
        arr = [1, 2, 3, 4, 5]
        k = 4
        x = 3
        expected_output = [1, 2, 3, 4]
        self.assertEqual(self.solution.findClosestElements(arr, k, x), expected_output)

    def test_findClosestElements_example2(self):
        arr = [1, 2, 3, 4, 5]
        k = 4
        x = -1
        expected_output = [1, 2, 3, 4]
        self.assertEqual(self.solution.findClosestElements(arr, k, x), expected_output)

    def test_findClosestElements_example3(self):
        arr = [1]
        k = 1
        x = 1
        expected_output = [1]
        self.assertEqual(self.solution.findClosestElements(arr, k, x), expected_output)

    def test_findClosestElements_custom(self):
        arr = [1, 1, 1, 10, 10, 10]
        k = 1
        x = 9
        expected_output = [10]
        self.assertEqual(self.solution.findClosestElements(arr, k, x), expected_output)

    def test_findClosestElements_custom2(self):
        arr = [1, 1, 2, 2, 2, 2, 2, 3, 3]
        k = 3
        x = 3
        expected_output = [2, 3, 3]
        self.assertEqual(self.solution.findClosestElements(arr, k, x), expected_output)

    def test_findClosestElements_custom3(self):
        arr = [1, 2]
        k = 1
        x = 1
        expected_output = [1]
        self.assertEqual(self.solution.findClosestElements(arr, k, x), expected_output)

    def test_findClosestElements_custom4(self):
        arr = [0, 0, 0, 1, 3, 5, 6, 7, 8, 8]
        k = 2
        x = 2
        expected_output = [1, 3]
        self.assertEqual(self.solution.findClosestElements(arr, k, x), expected_output)


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1
        while r - l >= k:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1
            else:
                l += 1
        return arr[l : r + 1]


class SSolution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diffs = [0] * len(arr)
        for r in range(len(arr)):  # [1, 1, 1, 10, 10, 10]
            diffs[r] = (abs(arr[r] - x), r)
        diffs.sort(key=lambda v: v[0])
        l, r = diffs[0][1], diffs[0][1]
        while l >= 0 and r < len(arr):
            if r - l + 1 == k:
                break
            if r == len(arr) - 1:
                l -= 1
            elif l == 0:
                r += 1
            elif abs(arr[r + 1] - x) < abs(arr[l - 1] - x):
                r += 1
            else:
                l -= 1
        return arr[l : r + 1]


if __name__ == "__main__":
    unittest.main()
