import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findDifferentBinaryString_example1(self):
        nums = ["01", "10"]
        expected_outputs = ["11", "00"]  # Both are correct
        result = self.solution.findDifferentBinaryString(nums)
        self.assertIn(
            result,
            expected_outputs,
            f"Failed on Example 1 with {result} not in {expected_outputs}",
        )

    def test_findDifferentBinaryString_example2(self):
        nums = ["00", "01"]
        expected_outputs = ["11", "10"]  # Both are correct
        result = self.solution.findDifferentBinaryString(nums)
        self.assertIn(
            result,
            expected_outputs,
            f"Failed on Example 2 with {result} not in {expected_outputs}",
        )

    def test_findDifferentBinaryString_example3(self):
        nums = ["111", "011", "001"]
        expected_outputs = ["101", "000", "010", "100", "110"]  # All are correct
        result = self.solution.findDifferentBinaryString(nums)
        self.assertIn(
            result,
            expected_outputs,
            f"Failed on Example 3 with {result} not in {expected_outputs}",
        )


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        numsSet = set()
        for n in nums:
            numsSet.add(n)

        def dfs(s):
            if len(s) == len(nums[0]):
                if s not in numsSet:
                    return s
                return ""

            res = dfs(s + "0")
            if res != "":
                return res
            res = dfs(s + "1")
            if res != "":
                return res
            return ""

        return dfs("")


if __name__ == "__main__":
    unittest.main()
