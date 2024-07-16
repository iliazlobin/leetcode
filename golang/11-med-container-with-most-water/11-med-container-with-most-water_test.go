package main

import (
	"testing"
)

func maxArea(height []int) int {
	maxArea := 0
	l, r := 0, len(height)-1
	for l < r {
		h := height[l]
		if height[r] < h {
			h = height[r]
		}
		area := h * (r - l)
		if area > maxArea {
			maxArea = area
		}

		if height[l] < height[r] {
			l += 1
		} else {
			r -= 1
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
