import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_singleNumber(self):
        nums = [3,2,3]
        result = self.solution.singleNumber(nums)
        self.assertEqual(result, 2)

        nums = [7,6,6,7,8]
        result = self.solution.singleNumber(nums)
        self.assertEqual(result, 8)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

if __name__ == "__main__":
    unittest.main()
