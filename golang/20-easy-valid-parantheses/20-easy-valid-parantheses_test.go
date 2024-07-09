package main

import (
	"testing"
)

func isValid(s string) bool {
	stack := []rune{}
	for _, c := range s {
		switch c {
		case '(', '[', '{':
			stack = append(stack, c)
		case ')', ']', '}':
			if len(stack) == 0 {
				return false
			}
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if !((top == '(' && c == ')') || (top == '[' && c == ']') || (top == '{' && c == '}')) {
				return false
			}
		}
	}
	return len(stack) == 0
}

func TestIsValid(t *testing.T) {
	testCases := []struct {
		input    string
		expected bool
	}{
		{"()", true},
		{"()[]{}", true},
		{"(]", false},
	}

	for _, tc := range testCases {
		actual := isValid(tc.input)
		if actual != tc.expected {
			t.Errorf("isValid(%q) = %v, expected %v", tc.input, actual, tc.expected)
		}
	}
}
