import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_missingNumber(self):
        nums = [1,2,3]
        result = self.solution.missingNumber(nums)
        self.assertEqual(result, 0)

        nums = [0,2]
        result = self.solution.missingNumber(nums)
        self.assertEqual(result, 1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) + 1):
            res = res ^ i
        print()
        for n in nums:
            res = res ^ n
        return res

if __name__ == "__main__":
    unittest.main()

