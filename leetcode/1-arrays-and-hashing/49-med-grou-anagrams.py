import unittest
from collections import Counter, defaultdict
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_groupAnagrams(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(len(result), 3)
        self.assertTrue(["eat", "tea", "ate"] in result)
        self.assertTrue(["tan", "nat"] in result)
        self.assertTrue(["bat"] in result)

        strs = [""]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(list(result), [[""]])

        strs = ["a"]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(list(result), [["a"]])


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for c in s:
                n = ord(c) - ord("a")
                count[n] += 1

            hashMap[tuple(count)].append(s)
        return list(hashMap.values())


if __name__ == "__main__":
    unittest.main()
