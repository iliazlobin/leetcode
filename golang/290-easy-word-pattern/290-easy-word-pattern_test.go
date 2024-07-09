package main

import (
	"strings"
	"testing"
)

func wordPattern(pattern string, s string) bool {
	fields := strings.Fields(s)
	if len(fields) != len(pattern) {
		return false
	}
	hMap := make(map[rune]string)
	rMap := make(map[string]rune)
	for i, c := range pattern {
		substr := fields[i]
		if m, ok := hMap[c]; ok {
			if m != substr {
				return false
			}
		}
		hMap[c] = substr
		if m, ok := rMap[substr]; ok {
			if m != c {
				return false
			}
		}
		rMap[substr] = c
	}
	return true
}

func TestWordPattern(t *testing.T) {
	testCases := []struct {
		pattern  string
		s        string
		expected bool
	}{
		{"abba", "dog cat cat dog", true},
		{"abba", "dog cat cat fish", false},
		{"aaaa", "dog cat cat dog", false},
		{"abba", "dog dog dog dog", false},
		{"abab", "chicken beef chicken beef", true},
	}

	for _, tc := range testCases {
		actual := wordPattern(tc.pattern, tc.s)
		if actual != tc.expected {
			t.Errorf("wordPattern(%q, %q) = %v, expected %v", tc.pattern, tc.s, actual, tc.expected)
		}
	}
}
