import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge_example1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        expected_output = [1, 2, 2, 3, 5, 6]
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected_output)

    def test_merge_example2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        expected_output = [1]
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected_output)

    def test_merge_example3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        expected_output = [1]
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected_output)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m -= 1
        n -= 1
        for i in range(len(nums1) - 1, -1, -1):
            if (m >= 0 and n >= 0 and nums1[m] < nums2[n]) or m < 0:
                nums1[i] = nums2[n]
                n -= 1
            else:
                nums1[i] = nums1[m]
                m -= 1


if __name__ == "__main__":
    unittest.main()
