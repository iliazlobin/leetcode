import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rearrangeArray_example1(self):
        nums = [3, 1, -2, -5, 2, -4]
        expected_output = [3, -2, 1, -5, 2, -4]
        self.assertEqual(self.solution.rearrangeArray(nums), expected_output)

    def test_rearrangeArray_example2(self):
        nums = [-1, 1]
        expected_output = [1, -1]
        self.assertEqual(self.solution.rearrangeArray(nums), expected_output)


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        p = 0
        n = 0
        while p < len(nums) and n < len(nums):
            if nums[p] < 0:
                p += 1
                continue
            if nums[n] >= 0:
                n += 1
                continue
            res.append(nums[p])
            res.append(nums[n])
            p += 1
            n += 1
        return res


if __name__ == "__main__":
    unittest.main()
