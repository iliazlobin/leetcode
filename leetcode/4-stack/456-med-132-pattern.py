import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find132pattern_example1(self):
        self.assertFalse(self.solution.find132pattern([1, 2, 3, 4]))

    def test_find132pattern_example2(self):
        self.assertTrue(self.solution.find132pattern([3, 1, 4, 2]))

    def test_find132pattern_example3(self):
        self.assertTrue(self.solution.find132pattern([-1, 3, 2, 0]))

    def test_find132pattern_additional(self):
        self.assertTrue(self.solution.find132pattern([3, 5, 0, 3, 4]))

    def test_find132pattern_wrong_answer(self):
        self.assertFalse(self.solution.find132pattern([1, 2, 3, 4, -4, -3, -5, -1]))


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []

        minN = nums[0]
        for n in nums:  # [3, 5, 0, 3, 4]
            while stack and n >= stack[-1][0]:
                stack.pop()

            if stack and n > stack[-1][1] and n < stack[-1][0]:
                return True

            stack.append((n, minN))
            minN = min(minN, n)

        return False


if __name__ == "__main__":
    unittest.main()
