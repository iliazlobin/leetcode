import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # def test_example1(self):
    #     arr = [17, 18, 5, 4, 6, 1]
    #     expected_output = [18, 6, 6, 6, 1, -1]
    #     self.assertEqual(self.solution.replaceElements(arr), expected_output)

    def test_example2(self):
        arr = [400]
        expected_output = [-1]
        self.assertEqual(self.solution.replaceElements(arr), expected_output)


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        for i in range(len(arr) -1, -1, -1):
            arr[i], greatest = greatest, max(greatest, arr[i])
        return arr

if __name__ == "__main__":
    unittest.main()
