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


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums))]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for i, v in count.items():
            freq[v].append(i)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


if __name__ == "__main__":
    unittest.main()
