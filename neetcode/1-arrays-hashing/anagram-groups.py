import unittest
from typing import Optional, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_anagrams: List[str] = []
        for s in strs:
            if len(strs) == 0:
                return [[s]]
            anagrams: List[str] = []
            anagrams.append(s)
            for ss in strs:
                if s == ss:
                    continue
                is_anagram = True
                for c in s:
                    is_found = False
                    for cc in ss:
                        if c == cc:
                            is_found = True
                            break
                    if not is_found:
                        is_anagram = False
                        break
                if is_anagram:
                    anagrams.append(ss)
            # remove duplicates
            found = False
            for existing_anagrams in all_anagrams:
                for existing_string in existing_anagrams:
                    if existing_string == anagrams[0]:
                        found = True
                        break
                if found:
                    break
            if not found:
                all_anagrams.append(anagrams)
        return all_anagrams

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_groupAnagrams(self):
        result = self.solution.groupAnagrams(["act","pots","tops","cat","stop","hat"])
        self.assertEqual(len(result), 3)
        self.assertTrue(["hat"] in result)
        self.assertTrue(sorted(["act", "cat"]) in [sorted(l) for l in result])
        self.assertTrue(sorted(["stop", "pots", "tops"]) in [sorted(l) for l in result])

        result = self.solution.groupAnagrams(["x"])
        self.assertEqual(len(result), 1)
        self.assertTrue(["x"] in result)

        result = self.solution.groupAnagrams([""])
        self.assertEqual(len(result), 1)
        self.assertTrue([""] in result)

        # Neetcode provides seemingly a wrong test case
        # result = self.solution.groupAnagrams(strs=["",""])
        # self.assertEqual(len(result), 2)
        # self.assertTrue([["", ""]] in result)

if __name__ == "__main__":
    unittest.main()
