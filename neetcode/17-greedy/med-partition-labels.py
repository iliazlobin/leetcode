import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_partitionLabels(self):
        s = "xyxxyzbzbbisl"
        result = self.solution.partitionLabels(s)
        self.assertEqual(result, [5, 5, 1, 1, 1])

        s = "abcabc"
        result = self.solution.partitionLabels(s)
        self.assertEqual(result, [6])


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterMap = {l: i for i, l in enumerate(s)}
        lp, rp = 0, 0
        partitions = []
        count = 0
        while lp < len(s):
            cur = s[lp]
            count += 1
            newRp = letterMap[cur]
            rp = max(rp, newRp)
            if rp <= lp:
                partitions.append(count)
                count = 0
            lp += 1
        return partitions

if __name__ == "__main__":
    unittest.main()
