import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_numOfSubarrays_example1(self):
        arr = [2, 2, 2, 2, 5, 5, 5, 8]
        k = 3
        threshold = 4
        expected_output = 3
        self.assertEqual(
            self.solution.numOfSubarrays(arr, k, threshold), expected_output
        )

    def test_numOfSubarrays_example2(self):
        arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
        k = 3
        threshold = 5
        expected_output = 6
        self.assertEqual(
            self.solution.numOfSubarrays(arr, k, threshold), expected_output
        )


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = []
        l = 0
        total = 0
        for r in range(len(arr)):
            total += arr[r]
            avr = total / k
            if r - l + 1 >= k:
                if avr >= threshold:
                    res.append(avr)
                total -= arr[l]
                l += 1
        return len(res)

if __name__ == "__main__":
    unittest.main()
