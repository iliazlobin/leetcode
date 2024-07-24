import unittest
from collections import Counter, defaultdict
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_groupAnagrams_example1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(sorted(map(sorted, result)), sorted(map(sorted, expected)))

    def test_groupAnagrams_example2(self):
        strs = [""]
        expected = [[""]]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(sorted(map(sorted, result)), sorted(map(sorted, expected)))

    def test_groupAnagrams_example3(self):
        strs = ["a"]
        expected = [["a"]]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(sorted(map(sorted, result)), sorted(map(sorted, expected)))


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            chars = [0] * 26
            for c in s:
                n = ord(c) - ord("a")
                chars[n] += 1
            if tuple(chars) in groups:
                groups[tuple(chars)].append(s)
            else:
                groups[tuple(chars)] = [s]

        return list(groups.values())


class SSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                n = ord(c) - ord("a")
                count[n] += 1

            res[tuple(count)].append(s)

        return list(res.values())


if __name__ == "__main__":
    unittest.main()
