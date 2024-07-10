package main

import (
	"testing"
)

func isAnagram(s string, t string) bool {
	characters := make(map[rune]int)

	for _, c := range s {
		if _, ok := characters[c]; !ok {
			characters[c] = 0
		}
		characters[c] += 1
	}

	for _, c := range t {
		if _, ok := characters[c]; !ok {
			return false
		}
		characters[c] -= 1
		if characters[c] < 0 {
			return false
		}
	}

	for _, v := range characters {
		if v != 0 {
			return false
		}
	}

	return true
}

func TestIsAnagram(t *testing.T) {
	testCases := []struct {
		s        string
		t        string
		expected bool
	}{
		// {"anagram", "nagaram", true},
		// {"rat", "car", false},
		{"ab", "a", false},
	}

	for _, tc := range testCases {
		actual := isAnagram(tc.s, tc.t)
		if actual != tc.expected {
			t.Errorf("isAnagram(%q, %q) = %v, expected %v", tc.s, tc.t, actual, tc.expected)
		}
	}
}
