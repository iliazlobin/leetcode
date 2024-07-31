import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minimizeMax_example1(self):
        nums = [10, 1, 2, 7, 1, 3]
        p = 2
        expected_output = 1
        self.assertEqual(self.solution.minimizeMax(nums, p), expected_output)

    def test_minimizeMax_example2(self):
        nums = [4, 2, 1, 2]
        p = 1
        expected_output = 0
        self.assertEqual(self.solution.minimizeMax(nums, p), expected_output)


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()

        def isValid(threshold):
            i, count = 0, 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= threshold:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count == p:
                    return True
            return False

        l, r = 0, 10**9
        while l <= r:
            m = (l + r) // 2
            if isValid(m):
                r = m - 1
            else:
                l = m + 1
        return l


if __name__ == "__main__":
    unittest.main()
