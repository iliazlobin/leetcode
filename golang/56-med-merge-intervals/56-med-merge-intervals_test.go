package main

import (
	"reflect"
	"sort"
	"testing"
)

func merge(intervals [][]int) [][]int {
	if len(intervals) <= 1 {
		return [][]int{[]int(intervals[0])}
	}
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	res := [][]int{}
	prev := intervals[0]
	for i := 1; i < len(intervals); i++ {
		if intervals[i][0] <= prev[1] {
			if intervals[i][1] >= prev[1] {
				prev[1] = intervals[i][1]
			}
		} else {
			res = append(res, prev)
			prev = intervals[i]
		}
	}
	res = append(res, prev)
	return res
}

func TestMerge(t *testing.T) {
	testCases := []struct {
		intervals [][]int
		expected  [][]int
	}{
		{[][]int{{1, 3}, {2, 6}, {8, 10}, {15, 18}}, [][]int{{1, 6}, {8, 10}, {15, 18}}},
		{[][]int{{1, 4}, {4, 5}}, [][]int{{1, 5}}},
		{intervals: [][]int{{1, 4}, {0, 4}}, expected: [][]int{{0, 4}}},
		{intervals: [][]int{{1, 4}, {2, 3}}, expected: [][]int{{1, 4}}},
	}

	for _, tc := range testCases {
		actual := merge(tc.intervals)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("merge(%v) = %v, expected %v", tc.intervals, actual, tc.expected)
		}
	}
}
