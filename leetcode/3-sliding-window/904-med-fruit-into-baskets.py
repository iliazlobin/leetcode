import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_totalFruit_example1(self):
        fruits = [1, 2, 1]
        expected_output = 3
        self.assertEqual(self.solution.totalFruit(fruits), expected_output)

    def test_totalFruit_example2(self):
        fruits = [0, 1, 2, 2]
        expected_output = 3
        self.assertEqual(self.solution.totalFruit(fruits), expected_output)

    def test_totalFruit_example3(self):
        fruits = [1, 2, 3, 2, 2]
        expected_output = 4
        self.assertEqual(self.solution.totalFruit(fruits), expected_output)


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        count = {}
        total = 0
        l, r = 0, 0
        # [1, 2, 3, 2, 2]
        while r < len(fruits):
            count[fruits[r]] = count.get(fruits[r], 0) + 1
            total += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                total -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            res = max(res, total)
            r += 1
        return res


if __name__ == "__main__":
    unittest.main()
