package main

import (
	"fmt"
)

func recursiveFebonacci(n int) int {
	if n <= 1 {
		return n
	}
	return recursiveFebonacci(n-2) + recursiveFebonacci(n-1)
}

func iterativeFebonacci(n int) int {
	if n <= 1 {
		return n
	}

	var first = 0
	var second = 1
	var res = 0
	for i := 0; i < n-1; i++ {
		res = first + second
		first = second
		second = res
	}

	return res
}

func main() {
	testCases := []struct {
		n        int // input
		expected int // expected result
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

	failedTests := 0

	for _, tc := range testCases {
		actual := iterativeFebonacci(tc.n)
		if actual != tc.expected {
			fmt.Printf("Test failed: iterativeFebonacci(%d) = %d, expected %d\n", tc.n, actual, tc.expected)
			failedTests++
		}
	}

	if failedTests == 0 {
		fmt.Println("All tests passed!")
	} else {
		fmt.Printf("%d tests failed.\n", failedTests)
	}
}
