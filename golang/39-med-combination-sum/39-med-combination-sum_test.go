package main

import (
	"reflect"
	"testing"
)

func combinationSum(candidates []int, target int) [][]int {
	res := [][]int{}
	comb := []int{}

	var dfs func(i int, total int)

	dfs = func(i int, total int) {
		if total == target {
			cp := make([]int, len(comb))
			copy(cp, comb)
			res = append(res, cp)
			return
		}
		if total > target {
			return
		}
		if i == len(candidates) {
			return
		}

		comb = append(comb, candidates[i])
		dfs(i, total+candidates[i])
		comb = comb[:len(comb)-1]
		dfs(i+1, total)
	}

	dfs(0, 0)
	return res
}

func TestCombinationSum(t *testing.T) {
	testCases := []struct {
		candidates []int
		target     int
		expected   [][]int
	}{
		{
			candidates: []int{2, 3, 6, 7},
			target:     7,
			expected:   [][]int{{2, 2, 3}, {7}},
		},
		{
			candidates: []int{2, 3, 5},
			target:     8,
			expected:   [][]int{{2, 2, 2, 2}, {2, 3, 3}, {3, 5}},
		},
		{
			candidates: []int{2},
			target:     1,
			expected:   [][]int{},
		},
	}

	for _, tc := range testCases {
		actual := combinationSum(tc.candidates, tc.target)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("combinationSum(%v, %d) = %v, expected %v", tc.candidates, tc.target, actual, tc.expected)
		}
	}
}
