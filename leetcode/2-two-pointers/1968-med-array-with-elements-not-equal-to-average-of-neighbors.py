import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rearrangeArray_example1(self):
        nums = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 4, 5, 3]
        result = self.solution.rearrangeArray(nums)
        self.assertEqual(result, expected_output)

    def test_rearrangeArray_example2(self):
        nums = [6, 2, 0, 9, 7]
        expected_output = [9, 7, 6, 2, 0]
        result = self.solution.rearrangeArray(nums)
        self.assertEqual(result, expected_output)


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [0] * len(nums)
        j = 1
        for n in nums:
            res[j] = n
            j += 2
            if j >= len(nums):
                j = 0
        return res


if __name__ == "__main__":
    unittest.main()
