import unittest
from collections import Counter, defaultdict
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isAnagram(self):
        s = "anagram"
        t = "nagaram"
        self.assertEqual(self.solution.isAnagram(s, t), True)

        s = "rat"
        t = "car"
        self.assertEqual(self.solution.isAnagram(s, t), False)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = defaultdict(int)
        for i in range(len(s)):
            chars[s[i]] += 1
            chars[t[i]] -= 1
        for _, v in chars.items():
            if v != 0:
                return False
        return True

class SSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 0 or len(s) != len(t):
            return False
        hashMap = {}
        for i in range(len(s)):
            sc = s[i]
            tc = t[i]
            if sc in hashMap:
                hashMap[sc] = hashMap[sc] + 1
            else:
                hashMap[sc] = 1
            if tc in hashMap:
                hashMap[tc] = hashMap[tc] - 1
            else:
                hashMap[tc] = -1
        for k, v in hashMap.items():
            if v != 0:
                return False
        return True


if __name__ == "__main__":
    unittest.main()
