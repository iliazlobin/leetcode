import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_checkSubarraySum_example1(self):
        nums = [23, 2, 4, 6, 7]
        k = 6
        expected_output = True
        self.assertEqual(self.solution.checkSubarraySum(nums, k), expected_output)

    def test_checkSubarraySum_example2(self):
        nums = [23, 2, 6, 4, 7]
        k = 6
        expected_output = True
        self.assertEqual(self.solution.checkSubarraySum(nums, k), expected_output)

    def test_checkSubarraySum_example3(self):
        nums = [23, 2, 6, 4, 7]
        k = 13
        expected_output = False
        self.assertEqual(self.solution.checkSubarraySum(nums, k), expected_output)

    def test_checkSubarraySum_example4(self):
        nums = [23, 2, 4, 6, 6]
        k = 7
        expected_output = True
        self.assertEqual(self.solution.checkSubarraySum(nums, k), expected_output)


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0: -1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            rem = total % k
            if rem in remainders and i - remainders[rem] > 1:
                return True
            remainders[rem] = i
        return False


if __name__ == "__main__":
    unittest.main()
