package main

import "testing"

// 0, 1, 1, 2, 3, 5, 8, 13
func iterativeFebonacci(n int) int {
	if n <= 1 {
		return n
	}

	first := 0
	second := 1
	res := 0
	for ; n > 1; n -= 1 {
		res = first + second
		first = second
		second = res
	}
	return res
}

func TestIterativeFebonacci(t *testing.T) {
	testCases := []struct {
		n        int
		expected int
	}{
		{0, 0},
		{1, 1},
		{2, 1},
		{3, 2},
		{4, 3},
		{5, 5},
		{6, 8},
		{7, 13},
	}

	for _, tc := range testCases {
		actual := iterativeFebonacci(tc.n)
		if actual != tc.expected {
			t.Errorf("iterativeFebonacci(%d) = %d, expected %d", tc.n, actual, tc.expected)
		}
	}
}
