import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isValid(self):
        print()


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = [0] * 2 * len(nums)
        for i, n in enumerate(nums):
            arr[i], arr[i + len(nums)] = n, n
        return arr


if __name__ == "__main__":
    unittest.main()
