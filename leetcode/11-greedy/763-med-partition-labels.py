import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_partitionLabels(self):
        # Example 1
        s = "ababcbacadefegdehijhklij"
        expected = [9, 7, 8]
        self.assertEqual(
            self.solution.partitionLabels(s), expected, "Failed for Example 1"
        )

        # Example 2
        s = "eccbbbbdec"
        expected = [10]
        self.assertEqual(
            self.solution.partitionLabels(s), expected, "Failed for Example 2"
        )


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = {}
        for i, c in enumerate(s):
            index[c] = i

        res = []
        splitIndex = 0
        prevSplitIndex = 0
        for i, c in enumerate(s):
            if splitIndex < i:
                res.append(i - prevSplitIndex)
                prevSplitIndex = i
            if index[c] > i:
                splitIndex = max(splitIndex, index[c])
        res.append(len(s) - prevSplitIndex)

        return res

if __name__ == "__main__":
    unittest.main()
