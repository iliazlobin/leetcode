package main

import (
	"sort"
	"testing"
)

func findMinArrowShots(points [][]int) int {
	sort.Slice(points, func(i, j int) bool {
		return points[i][0] < points[j][0]
	})

	res := 1
	// var target []int
	target := make([]int, 2)
	for p, point := range points {
		if p == 0 {
			// target = point
			copy(target, point)
		}
		if point[0] <= target[1] {
			if point[0] > target[0] {
				target[0] = point[0]
			}
			if point[1] < target[1] {
				target[1] = point[1]
			}
		} else {
			res++
			// target = point
			copy(target, point)
		}
	}
	return res
}

func TestFindMinArrowShots(t *testing.T) {
	testCases := []struct {
		points   [][]int
		expected int
	}{
		{
			points:   [][]int{{10, 16}, {2, 8}, {1, 6}, {7, 12}},
			expected: 2,
		},
		{
			points:   [][]int{{1, 2}, {3, 4}, {5, 6}, {7, 8}},
			expected: 4,
		},
		{
			points:   [][]int{{1, 2}, {2, 3}, {3, 4}, {4, 5}},
			expected: 2,
		},
	}

	for _, tc := range testCases {
		actual := findMinArrowShots(tc.points)
		if actual != tc.expected {
			t.Errorf("findMinArrowShots(%v) = %d, expected %d", tc.points, actual, tc.expected)
		}
	}
}
