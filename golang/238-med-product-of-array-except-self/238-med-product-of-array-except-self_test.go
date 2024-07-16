package main

import (
	"testing"
)

func productExceptSelf(nums []int) []int {
	leftProducts := make([]int, len(nums))
	rightProducts := make([]int, len(nums))

	for i, j := 0, len(nums)-1; i < len(nums); i, j = i+1, j-1 {
		if i == 0 {
			leftProducts[0] = nums[0]
		} else {
			leftProducts[i] = leftProducts[i-1] * nums[i]
		}
		if j == len(nums)-1 {
			rightProducts[j] = nums[len(nums)-1]
		} else {
			rightProducts[j] = rightProducts[j+1] * nums[j]
		}
	}

	res := make([]int, len(nums))
	for i := 0; i < len(nums); i += 1 {
		leftProduct := 1
		if i > 0 {
			leftProduct = leftProducts[i-1]
		}
		rightProduct := 1
		if i < len(nums)-1 {
			rightProduct = rightProducts[i+1]
		}
		res[i] = leftProduct * rightProduct
	}

	return res
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
