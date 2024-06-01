import unittest
from typing import List, Optional


class Solution:
    separator = "!@#$%@#@!"

    def encode(self, strs: List[str]) -> str:
        long_string = self.separator.join(strs)
        if long_string == "":
            if len(strs) > 0:
                long_string = self.separator
        return long_string

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        if s == self.separator:
            return [""]
        return s.split(self.separator)


class Solution2:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += "[" + str(len(s)) + "]" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        text = s
        while len(text) > 0:
            index_left = text.find("[")
            next_text = text[index_left + 1 :]
            index_right = next_text.find("]")
            length = int(next_text[:index_right])
            processed_next_text = next_text[index_right + 1 :]
            element = processed_next_text[:length]
            res.append(element)
            text = processed_next_text[length:]
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test_encode_decode(self):
        original = ["neet", "code", "love", "you"]
        encoded = self.solution.encode(original)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, original)

        original = ["we","say",":","yes"]
        encoded = self.solution.encode(original)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, original)

        original = []
        encoded = self.solution.encode(original)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, original)

        original = [""]
        encoded = self.solution.encode(original)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, original)

        original = ["we", "say", ":", "yes", "!@#$%^&*()"]
        encoded = self.solution.encode(original)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, original)

        original = ["#", "##"]
        encoded = self.solution.encode(original)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, original)


if __name__ == "__main__":
    unittest.main()
