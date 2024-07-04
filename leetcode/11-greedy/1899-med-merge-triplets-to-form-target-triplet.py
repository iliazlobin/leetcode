import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_mergeTriplets(self):
        # Example 1
        triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
        target = [2, 7, 5]
        self.assertTrue(
            self.solution.mergeTriplets(triplets, target), "Failed for Example 1"
        )

        # Example 2
        triplets = [[3, 4, 5], [4, 5, 6]]
        target = [3, 2, 5]
        self.assertFalse(
            self.solution.mergeTriplets(triplets, target), "Failed for Example 2"
        )

        # Example 3
        triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
        target = [5, 5, 5]
        self.assertTrue(
            self.solution.mergeTriplets(triplets, target), "Failed for Example 3"
        )


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]
        for triplet in triplets:
            if (
                triplet[0] > target[0]
                or triplet[1] > target[1]
                or triplet[2] > target[2]
            ):
                continue
            res = [
                max(res[0], triplet[0]),
                max(res[1], triplet[1]),
                max(res[2], triplet[2]),
            ]

        return res[0] == target[0] and res[1] == target[1] and res[2] == target[2]


if __name__ == "__main__":
    unittest.main()
