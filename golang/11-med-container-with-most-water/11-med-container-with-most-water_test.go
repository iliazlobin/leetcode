package main

import (
	"testing"
)

func maxArea(height []int) int {
	r := len(height) - 1
	maxArea := 0
	for l := 0; l < r; {
		curHeight := height[l]
		if height[r] < curHeight {
			curHeight = height[r]
		}
		area := (r - l) * curHeight
		if area > maxArea {
			maxArea = area
		}

		if height[l] < height[r] {
			l++
		} else {
			r--
		}
	}
	return maxArea
}

func TestMaxArea(t *testing.T) {
	testCases := []struct {
		height   []int
		expected int
	}{
		{[]int{1, 8, 6, 2, 5, 4, 8, 3, 7}, 49},
		{[]int{1, 1}, 1},
	}

	for _, tc := range testCases {
		actual := maxArea(tc.height)
		if actual != tc.expected {
			t.Errorf("maxArea(%v) = %d, expected %d", tc.height, actual, tc.expected)
		}
	}
}
