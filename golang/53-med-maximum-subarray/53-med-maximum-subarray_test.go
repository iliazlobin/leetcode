package main

import (
	"testing"
	"math"
)

func maxSubArray(nums []int) int {
	localMax := math.MinInt
}

func TestMaxSubArray(t *testing.T) {
	testCases := []struct {
		nums     []int
		expected int
	}{
		{nums: []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}, expected: 6},
		{nums: []int{1}, expected: 1},
		{nums: []int{5, 4, -1, 7, 8}, expected: 23},
	}

	for _, tc := range testCases {
		actual := maxSubArray(tc.nums)
		if actual != tc.expected {
			t.Errorf("maxSubArray(%v) = %v, expected %v", tc.nums, actual, tc.expected)
		}
	}
}
