package main

import (
	"reflect"
	"testing"
)

func combine(n int, k int) [][]int {
	res := [][]int{}

	var dfs func(l int, comb []int)

	dfs = func(l int, comb []int) {
		if len(comb) == k {
			combCopy := make([]int, len(comb))
			copy(combCopy, comb)
			res = append(res, combCopy)
			return
		}
		if l > n {
			return
		}

		comb = append(comb, l)
		dfs(l+1, comb)
		comb = comb[:len(comb)-1]
		dfs(l+1, comb)
	}

	dfs(1, []int{})
	return res
}

func TestCombine(t *testing.T) {
	testCases := []struct {
		n        int
		k        int
		expected [][]int
	}{
		{
			n: 4,
			k: 2,
			expected: [][]int{
				{1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4},
			},
		},
		{
			n:        1,
			k:        1,
			expected: [][]int{{1}},
		},
	}

	for _, tc := range testCases {
		actual := combine(tc.n, tc.k)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("combine(%d, %d) = %v, expected %v", tc.n, tc.k, actual, tc.expected)
		}
	}
}
