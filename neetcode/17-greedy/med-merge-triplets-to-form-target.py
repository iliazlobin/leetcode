import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_mergeTriplets(self):
        triplets = [[1, 2, 3], [7, 1, 1]]
        target = [7, 2, 3]
        result = self.solution.mergeTriplets(triplets, target)
        self.assertTrue(result)

        triplets = [[2, 5, 6], [1, 4, 4], [5, 7, 5]]
        target = [5, 4, 6]
        result = self.solution.mergeTriplets(triplets, target)
        self.assertFalse(result)


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 0:
            return False
        curTriplet = triplets[0]
        for triplet in triplets[1:]:
            skip = False
            for i in range(0, 3):
                if triplet[i] > target[i]:
                    skip = True
                    break
            if skip:
                continue
            curTriplet = [
                max(curTriplet[0], triplet[0]),
                max(curTriplet[1], triplet[1]),
                max(curTriplet[2], triplet[2]),
            ]
        for i in range(0, 3):
            if curTriplet[i] != target[i]:
                return False
        return True


if __name__ == "__main__":
    unittest.main()
