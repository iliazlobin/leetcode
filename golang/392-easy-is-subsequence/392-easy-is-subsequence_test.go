package main

import (
	"testing"
)

func isSubsequence(s string, t string) bool {
	if len(s) == 0 {
		return true
	}
	p := 0
	for i := range t {
		if s[p] == t[i] {
			p += 1
		}
		if p == len(s) {
			return true
		}
	}
	return false
}

func TestIsSubsequence(t *testing.T) {
	testCases := []struct {
		s        string
		t        string
		expected bool
	}{
		{"", "ahbgdc", true},
		{"abc", "ahbgdc", true},
		{"axc", "ahbgdc", false},
	}

	for _, tc := range testCases {
		actual := isSubsequence(tc.s, tc.t)
		if actual != tc.expected {
			t.Errorf("isSubsequence(%q, %q) = %v, expected %v", tc.s, tc.t, actual, tc.expected)
		}
	}
}
