package main

import (
	"testing"
)

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	} else if len(strs) == 1 {
		return strs[0]
	} else if len(strs[0]) == 0 {
		return ""
	}

	l := 0
outer:
	for l < len(strs[0]) {
		c := strs[0][l]
		for i := 1; i < len(strs); i += 1 {
			if l == len(strs[i]) || strs[i][l] != c {
				break outer
			}
		}

		l += 1
	}

	return strs[0][:l]
}

func TestLongestCommonPrefix(t *testing.T) {
	testCases := []struct {
		input    []string
		expected string
	}{
		// {[]string{"flower", "flow", "flight"}, "fl"},
		// {[]string{"dog", "racecar", "car"}, ""},
		{[]string{"ab", "a"}, "a"},
	}

	for _, tc := range testCases {
		actual := longestCommonPrefix(tc.input)
		if actual != tc.expected {
			t.Errorf("longestCommonPrefix(%v) = %s, expected %s", tc.input, actual, tc.expected)
		}
	}
}
