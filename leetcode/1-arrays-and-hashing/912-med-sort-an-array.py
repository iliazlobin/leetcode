import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sortArray_example1(self):
        nums = [5, 2, 3, 1]
        expected = [1, 2, 3, 5]
        result = self.solution.sortArray(nums)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_sortArray_example2(self):
        nums = [5, 1, 1, 2, 0, 0]
        expected = [0, 0, 1, 1, 2, 5]
        result = self.solution.sortArray(nums)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            left, right = arr[l : m + 1], arr[m + 1 : r + 1]
            i, l, r = l, 0, 0

            while l < len(left) or r < len(right):
                if r == len(right) or (l < len(left) and left[l] <= right[r]):
                    arr[i] = left[l]
                    l += 1
                elif l == len(left) or (r < len(right) and right[r] < left[l]):
                    arr[i] = right[r]
                    r += 1
                i += 1

        def mergeSort(arr, l, r):
            if l == r:
                return arr

            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)

            merged = merge(arr, l, m, r)
            return merged

        mergeSort(nums, 0, len(nums) - 1)
        return nums


class BSolution:
    def sortArray(self, nums: List[int]) -> List[int]:
        i = 0
        for i in range(len(nums) - 1, 0, -1):
            for j in range(0, i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums


if __name__ == "__main__":
    unittest.main()
