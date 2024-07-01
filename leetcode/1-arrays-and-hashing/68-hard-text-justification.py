import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_fullJustify(self):
        words1 = ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth1 = 16
        expected1 = ["This    is    an", "example  of text", "justification.  "]
        self.assertEqual(
            self.solution.fullJustify(words1, maxWidth1), expected1, "Example 1 failed"
        )

        words2 = ["What", "must", "be", "acknowledgment", "shall", "be"]
        maxWidth2 = 16
        expected2 = ["What   must   be", "acknowledgment  ", "shall be        "]
        self.assertEqual(
            self.solution.fullJustify(words2, maxWidth2), expected2, "Example 2 failed"
        )

        words3 = [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ]
        maxWidth3 = 20
        expected3 = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  ",
        ]
        self.assertEqual(
            self.solution.fullJustify(words3, maxWidth3), expected3, "Example 3 failed"
        )


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                extraSpaces = maxWidth - length
                spaces = extraSpaces // max(1, (len(line) - 1))
                leftSpaces = extraSpaces % max(1, (len(line) - 1))
                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces
                    if leftSpaces > 0:
                        line[j] += " "
                        leftSpaces -= 1
                # out += line[-1]
                res.append("".join(line))

                line = []
                length = 0

            line.append(words[i])
            length += len(words[i])
            i += 1

        out = ""
        for j in range(len(line) - 1):
            out += line[j] + " "
        out += line[-1]
        out += " " * (maxWidth - length - len(line) + 1)
        res.append(out)

        return res


if __name__ == "__main__":
    unittest.main()
