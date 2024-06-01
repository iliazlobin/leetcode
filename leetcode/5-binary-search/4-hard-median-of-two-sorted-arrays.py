import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findMedianSortedArrays(self):
        nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
        nums2 = [1, 2, 3, 4]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 3.5)

        nums1 = [1, 3]
        nums2 = [2]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 2.0)

        nums1 = [1, 2]
        nums2 = [3, 4]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 2.5)


# log(min(n, m))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i: int = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


if __name__ == "__main__":
    unittest.main()
