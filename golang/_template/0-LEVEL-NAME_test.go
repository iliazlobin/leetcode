package main

import (
	"testing"
)

func isPalindrome(n int) error {
	return nil
}

func TestIsPalindrome(t *testing.T) {
	testCases := []struct {
		input    int
		expected bool
	}{
		{121, true},
		{-121, false},
		{10, false},
	}

	for _, tc := range testCases {
		actual := isPalindrome(tc.input)
		if actual != tc.expected {
			t.Errorf("isPalindrome(%d) = %v, expected %v", tc.input, actual, tc.expected)
		}
	}
}
