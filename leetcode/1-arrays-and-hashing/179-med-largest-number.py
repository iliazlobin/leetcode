import unittest
from collections import Counter
from typing import List, Optional
from functools import cmp_to_key


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_largestNumber_example1(self):
        nums = [10, 2]
        expected_output = "210"
        self.assertEqual(self.solution.largestNumber(nums), expected_output)

    def test_largestNumber_example2(self):
        nums = [3, 30, 34, 5, 9]
        expected_output = "9534330"
        self.assertEqual(self.solution.largestNumber(nums), expected_output)


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))


if __name__ == "__main__":
    unittest.main()
