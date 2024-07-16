package main

import (
	"testing"
)

func trailingZeroes(n int) int {
	res := 0
	for n > 0 {
		n /= 5
		res += n
	}
	return res
}

func factorial(n int) int {
	if n <= 2 {
		return n
	}

	return n * factorial(n-1)
}

func TestTrailingZeroes(t *testing.T) {
	testCases := []struct {
		input    int
		expected int
	}{
		// {3, 0},
		// {5, 1},
		// {0, 0},
		{30, 7},
	}

	for _, tc := range testCases {
		actual := trailingZeroes(tc.input)
		if actual != tc.expected {
			t.Errorf("trailingZeroes(%d) = %d, expected %d", tc.input, actual, tc.expected)
		}
	}
}
