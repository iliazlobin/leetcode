import unittest
from collections import Counter, deque
from typing import List, Optional


class TestUniformIntegerCount(unittest.TestCase):
    def test_uniform_integer_count_case1(self):
        A, B = 75, 300
        expected = 5
        result = getUniformIntegerCountInInterval(A, B)
        self.assertEqual(expected, result)

    def test_uniform_integer_count_case2(self):
        A, B = 1, 9
        expected = 9
        result = getUniformIntegerCountInInterval(A, B)
        self.assertEqual(expected, result)

    def test_uniform_integer_count_case3(self):
        A, B = 999999999999, 999999999999
        expected = 1
        result = getUniformIntegerCountInInterval(A, B)
        self.assertEqual(expected, result)


def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    uniform_numbers = []

    for digit in range(1, 10):
        num = digit
        while num <= 10**12:
            uniform_numbers.append(num)
            num = num * 10 + digit

    count = 0
    for number in uniform_numbers:
        if A <= number <= B:
            count += 1

    return count


if __name__ == "__main__":
    unittest.main()
