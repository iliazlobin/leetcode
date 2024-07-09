package main

import (
	"testing"
)

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	i := 0
	res := -1
	stop := false
	for true {
		c := byte(0)
		for j, s := range strs {
			if i == len(s) {
				stop = true
				break
			}
			if j == 0 {
				c = s[i]
			} else {
				if c != s[i] {
					stop = true
					break
				}
			}
		}
		if stop {
			break
		}
		res = i
		i += 1
	}
	return strs[0][:res+1]
}

func TestLongestCommonPrefix(t *testing.T) {
	testCases := []struct {
		input    []string
		expected string
	}{
		{[]string{"flower", "flow", "flight"}, "fl"},
		{[]string{"dog", "racecar", "car"}, ""},
	}

	for _, tc := range testCases {
		actual := longestCommonPrefix(tc.input)
		if actual != tc.expected {
			t.Errorf("longestCommonPrefix(%v) = %s, expected %s", tc.input, actual, tc.expected)
		}
	}
}
