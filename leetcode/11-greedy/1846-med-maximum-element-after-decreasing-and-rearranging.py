import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maximumElementAfterDecrementingAndRearranging_example1(self):
        arr = [2, 2, 1, 2, 1]
        expected = 2
        result = self.solution.maximumElementAfterDecrementingAndRearranging(arr)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_maximumElementAfterDecrementingAndRearranging_example2(self):
        arr = [100, 1, 1000]
        expected = 3
        result = self.solution.maximumElementAfterDecrementingAndRearranging(arr)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )

    def test_maximumElementAfterDecrementingAndRearranging_example3(self):
        arr = [1, 2, 3, 4, 5]
        expected = 5
        result = self.solution.maximumElementAfterDecrementingAndRearranging(arr)
        self.assertEqual(
            expected, result, f"Failed on Example 3 with {result} != {expected}"
        )

    def test_maximumElementAfterDecrementingAndRearranging_custom(self):
        arr = [73, 98, 9]
        expected = 3
        result = self.solution.maximumElementAfterDecrementingAndRearranging(arr)
        self.assertEqual(
            expected, result, f"Failed on custom test with {result} != {expected}"
        )


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr = sorted(arr)
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1
        return arr[len(arr) - 1]


if __name__ == "__main__":
    unittest.main()
