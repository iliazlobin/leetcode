package main

import (
	"reflect"
	"testing"
)

var letters = map[string][]string{
	"1": {},
	"2": {"a", "b", "c"},
	"3": {"d", "e", "f"},
	"4": {"g", "h", "i"},
	"5": {"j", "k", "l"},
	"6": {"m", "n", "o"},
	"7": {"p", "q", "r", "s"},
	"8": {"t", "u", "v"},
	"9": {"w", "x", "y", "z"},
}

func letterCombinations(digits string) []string {
	res := []string{}
	var dfs func(i int, cur string)
	dfs = func(i int, cur string) {
		if i == len(digits) {
			if len(cur) > 0 {
				res = append(res, cur)
			}
			return
		}
		digit := digits[i:i+1]
		for _, c := range letters[digit] {
			dfs(i+1, cur+c)
		}
	}
	dfs(0, "")
	return res
}

func TestLetterCombinations(t *testing.T) {
	testCases := []struct {
		digits   string
		expected []string
	}{
		{"23", []string{"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}},
		{"", []string{}},
		{"2", []string{"a", "b", "c"}},
	}

	for _, tc := range testCases {
		actual := letterCombinations(tc.digits)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("letterCombinations(%q) = %v, expected %v", tc.digits, actual, tc.expected)
		}
	}
}
