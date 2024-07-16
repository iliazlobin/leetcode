package main

import (
	"strings"
	"testing"
)

func reverseWords(s string) string {
	parts := strings.Fields(s)
	for i, j := 0, len(parts)-1; i < j; i, j = i+1, j-1 {
		parts[i], parts[j] = parts[j], parts[i]
	}
	return strings.Join(parts, " ")
}

func TestReverseWords(t *testing.T) {
	testCases := []struct {
		input    string
		expected string
	}{
		{
			input:    "the sky is blue",
			expected: "blue is sky the",
		},
		{
			input:    "  hello world  ",
			expected: "world hello",
		},
		{
			input:    "a good   example",
			expected: "example good a",
		},
	}

	for _, tc := range testCases {
		actual := reverseWords(tc.input)
		if actual != tc.expected {
			t.Errorf("reverseWords(%q) = %q, expected %q", tc.input, actual, tc.expected)
		}
	}
}
