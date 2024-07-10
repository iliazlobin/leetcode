package main

import (
	"reflect"
	"strings"
	"testing"
)

func generateParenthesis(n int) []string {
	res := []string{}
	stack := []string{}

	var dfs func(open int, close int)
	dfs = func(open int, close int) {
		if open == n && close == n {
			res = append(res, strings.Join(stack, ""))
			return
		}

		if open < n {
			stack = append(stack, "(")
			dfs(open+1, close)
			stack = stack[:len(stack)-1]
		}
		if close < open {
			stack = append(stack, ")")
			dfs(open, close+1)
			stack = stack[:len(stack)-1]
		}
	}

	dfs(0, 0)
	return res
}

func TestGenerateParenthesis(t *testing.T) {
	testCases := []struct {
		n        int
		expected []string
	}{
		{
			n:        3,
			expected: []string{"((()))", "(()())", "(())()", "()(())", "()()()"},
		},
		{
			n:        1,
			expected: []string{"()"},
		},
	}

	for _, tc := range testCases {
		actual := generateParenthesis(tc.n)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("generateParenthesis(%d) = %v, expected %v", tc.n, actual, tc.expected)
		}
	}
}
