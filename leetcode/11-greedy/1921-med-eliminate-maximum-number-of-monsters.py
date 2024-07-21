import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_eliminateMaximum_example1(self):
        self.assertEqual(
            self.solution.eliminateMaximum([1, 3, 4], [1, 1, 1]), 3, "Example 1 failed."
        )

    def test_eliminateMaximum_example2(self):
        self.assertEqual(
            self.solution.eliminateMaximum([1, 1, 2, 3], [1, 1, 1, 1]),
            1,
            "Example 2 failed.",
        )

    def test_eliminateMaximum_example3(self):
        self.assertEqual(
            self.solution.eliminateMaximum([3, 2, 4], [5, 3, 2]), 1, "Example 3 failed."
        )

    def test_eliminateMaximum_custom(self):
        self.assertEqual(
            self.solution.eliminateMaximum([4, 3, 4], [1, 1, 2]),
            3,
            "Custom test case failed.",
        )

    def test_eliminateMaximum_given_case(self):
        dist = [5, 4, 3, 3, 3]
        speed = [1, 1, 5, 3, 1]
        expected = 1
        result = self.solution.eliminateMaximum(dist, speed)
        self.assertEqual(expected, result, "Given test case failed.")


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [d / s for d, s in zip(dist, speed)]
        res = 0
        clock = 0
        for t in sorted(time):
            if t > clock:
                res += 1
            else:
                break
            clock += 1
        return res


if __name__ == "__main__":
    unittest.main()
