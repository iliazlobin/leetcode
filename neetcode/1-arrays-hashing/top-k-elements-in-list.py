import unittest
from collections import Counter
from typing import List, Optional


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freq = 0
            if n in freqs:
                freq = freqs[n]["freq"]
            freq += 1
            freqs[n] = {
                "index": n,
                "freq": freq,
            }
        print(freqs)
        items = freqs.items()
        sorted_freqs = sorted(freqs.items(), key=lambda x: x[1]["freq"], reverse=True)
        print(sorted_freqs)
        most_freq = []
        for s in sorted_freqs[:k]:
            most_freq.append(s[1]["index"])
        return most_freq

    def topKFrequent_copilot(self, nums, k):
        counter = Counter(nums)
        freqs = [(num, freq) for num, freq in counter.items()]
        sorted_freqs = sorted(freqs, key=lambda x: x[1], reverse=True)
        return [num for num, freq in sorted_freqs[:k]]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_topKFrequent(self):
        result = self.solution.topKFrequent([1, 2, 2, 3, 3, 3], 2)
        self.assertEqual(len(result), 2)
        self.assertTrue(2 in result)
        self.assertTrue(3 in result)

        result = self.solution.topKFrequent([7, 7], 1)
        self.assertEqual(len(result), 1)
        self.assertTrue(7 in result)

        result = self.solution.topKFrequent_copilot([1, 1, 1, 2, 2, 3333], 2)
        self.assertEqual(len(result), 2)
        self.assertTrue(1 in result)
        self.assertTrue(2 in result)


if __name__ == "__main__":
    unittest.main()
