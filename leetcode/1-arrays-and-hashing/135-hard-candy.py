import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_candy(self):
        ratings1 = [1, 0, 2]
        self.assertEqual(self.solution.candy(ratings1), 5, "Example 1 failed")

        ratings2 = [1, 2, 2]
        self.assertEqual(self.solution.candy(ratings2), 4, "Example 2 failed")

        ratings = [1, 3, 4, 5, 2]
        self.assertEqual(
            self.solution.candy(ratings), 11, "Test with ratings=[1,3,4,5,2] failed"
        )


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        return sum(candies)


if __name__ == "__main__":
    unittest.main()
