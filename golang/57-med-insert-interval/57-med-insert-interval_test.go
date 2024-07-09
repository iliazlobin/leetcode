package main

import (
	"reflect"
	"testing"
)

func insert(intervals [][]int, newInterval []int) [][]int {
	res := [][]int{}

	for i := range intervals {
		if newInterval[1] < intervals[i][0] {
			res = append(res, newInterval)
			res = append(res, intervals[i:]...)
			return res
		} else if newInterval[0] > intervals[i][1] {
			res = append(res, intervals[i])
		} else {
			if intervals[i][0] < newInterval[0] {
				newInterval[0] = intervals[i][0]
			}
			if intervals[i][1] > newInterval[1] {
				newInterval[1] = intervals[i][1]
			}
		}
	}

	if len(res) > 0 {
		if newInterval[0] > res[len(res)-1][1] {
			res = append(res, newInterval)
		}
		return res
	} else {
		return [][]int{newInterval}
	}
}

func TestInsert(t *testing.T) {
	testCases := []struct {
		intervals   [][]int
		newInterval []int
		expected    [][]int
	}{
		{
			intervals:   [][]int{{1, 3}, {6, 9}},
			newInterval: []int{2, 5},
			expected:    [][]int{{1, 5}, {6, 9}},
		},
		{
			intervals:   [][]int{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}},
			newInterval: []int{4, 8},
			expected:    [][]int{{1, 2}, {3, 10}, {12, 16}},
		},
		{
			intervals:   [][]int{{1, 5}},
			newInterval: []int{6, 8},
			expected:    [][]int{{1, 5}, {6, 8}},
		},
		{
			intervals:   [][]int{{0, 2}, {3, 9}},
			newInterval: []int{6, 8},
			expected:    [][]int{{0, 2}, {3, 9}},
		},
	}

	for _, tc := range testCases {
		actual := insert(tc.intervals, tc.newInterval)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("insert(%v, %v) = %v, expected %v", tc.intervals, tc.newInterval, actual, tc.expected)
		}
	}
}
