import unittest
from collections import Counter, defaultdict
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.solution = NlogNSolution()
        self.solution = Solution()

    def test_topKFrequent(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        self.assertEqual(set(self.solution.topKFrequent(nums, k)), set([1, 2]))

        nums = [1]
        k = 1
        self.assertEqual(set(self.solution.topKFrequent(nums, k)), set([1]))

    def test_topKFrequent_customTest(self):
        nums = [3, 0, 1, 0]
        k = 1
        expected = [0]
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(
            expected,
            list(result),
            f"Failed with nums={nums} and k={k} where expected {expected} but got {list(result)}",
        )

    def test_topKFrequent_customTest(self):
        nums = [3, 0, 1, 0]
        k = 1
        expected = [0]
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(
            expected,
            list(result),
            f"Failed with nums={nums} and k={k} where expected {expected} but got {list(result)}",
        )


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for n in nums:
            hmap[n] = hmap.get(n, 0) + 1
        freqs = {n: [] for n in range(len(nums) + 1)}
        for i, v in hmap.items():
            freqs[v].append(i)

        res = []
        for f in range(len(freqs) - 1, -1, -1):
            for e in freqs[f]:
                k -= 1
                res.append(e)
                if k == 0:
                    return res


class NlogNSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            if n in hashMap:
                hashMap[n] = (n, hashMap[n][1] + 1)
            else:
                hashMap[n] = (n, 1)
        values = list(hashMap.values())
        values.sort(key=lambda p: p[1], reverse=True)
        return map(lambda p: p[0], values[:k])


if __name__ == "__main__":
    unittest.main()
