import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    # def setUp(self):
    #     self.solution = Solution()

    def test_kvstorage(self):
        kv = KVStorage()
        results = kv.process(
            [
                "SET k1 v1",
                "GET k1",  # Should return 'v1'
                "BEGIN",
                "SET k1 v2",
                "GET k1",  # Should return 'v2' after setting it in the transaction
                "ROLLBACK",
                "GET k1",  # Should return 'v1' after rollback
            ]
        )
        expected_results = ["v1", "v2", "v1"]
        self.assertEqual(results, expected_results)

    def test_kvstorage2(self):
        kv = KVStorage()
        results = kv.process(
            [
                "SET k1 v1",
                "GET k1",
                "BEGIN",
                "SET k1 v2",
                "GET k1",
                "BEGIN",
                "SET k1 v3",
                "GET k1",
                "COMMIT",
                "SET k1 v4",
                "GET k1",
                "ROLLBACK",
                "GET k1",
            ]
        )
        expected_results = ["v1", "v2", "v3", "v4", "v1"]
        self.assertEqual(results, expected_results)


class KVStorage:
    transactions = []
    kv = {}

    def process(self, lines):
        res = []
        for line in lines:
            c = line.split(" ", 1)[0]
            if c == "SET":
                _, k, v = line.split(" ")
                if k in self.kv:
                    self.kv[k].append(v)
                else:
                    self.kv[k] = [v]
            elif c == "GET":
                res.append(self.kv[k][-1])
            elif c == "BEGIN":
                snapshot = {}
                for k, v in self.kv.items():
                    snapshot[k] = len(v) - 1
                self.transactions.append(snapshot)
            elif c == "ROLLBACK":
                if len(self.transactions) == 0:
                    continue
                snapshot = self.transactions.pop()
                for k, v in snapshot.items():
                    self.kv[k] = self.kv[k][: v + 1]
                # print()
            elif c == "COMMIT":
                if len(self.transactions) == 0:
                    continue
                self.transactions.pop()
        return res


if __name__ == "__main__":
    unittest.main()
