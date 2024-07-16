package main

import (
	"testing"
)

func lengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	}
	res := 1
	set := make(map[rune]bool)
	set[rune(s[0])] = true
	l, r := 0, 0
	for {
		r += 1
		if r == len(s) {
			break
		}
		for {
			if _, ok := set[rune(s[r])]; ok {
				delete(set, rune(s[l]))
				l += 1
				continue
			}
			break
		}
		set[rune(s[r])] = true
		if r-l+1 > res {
			res = r - l + 1
		}
	}

	return res
}

func TestLengthOfLongestSubstring(t *testing.T) {
	testCases := []struct {
		input    string
		expected int
	}{
		{"abcabcbb", 3},
		{"bbbbb", 1},
		{"pwwkew", 3},
	}

	for _, tc := range testCases {
		actual := lengthOfLongestSubstring(tc.input)
		if actual != tc.expected {
			t.Errorf("lengthOfLongestSubstring(%q) = %d, expected %d", tc.input, actual, tc.expected)
		}
	}
}
