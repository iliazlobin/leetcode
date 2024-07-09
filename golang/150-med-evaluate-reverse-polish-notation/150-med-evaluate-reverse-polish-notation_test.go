package main

import (
	"strconv"
	"testing"
)

func evalRPN(tokens []string) int {
	stack := []int{}
	res := 0
	for _, t := range tokens {
		switch t {
		case "+", "-", "*", "/":
			right := stack[len(stack)-1]
			left := stack[len(stack)-2]
			stack = stack[:len(stack)-2]
			switch t {
			case "+":
				res = left + right
			case "-":
				res = left - right
			case "*":
				res = left * right
			case "/":
				res = int(left / right)
			}
			stack = append(stack, res)
		default:
			n, _ := strconv.Atoi(t)
			stack = append(stack, n)
		}
	}
	return stack[len(stack)-1]
}

func TestEvalRPN(t *testing.T) {
	testCases := []struct {
		tokens   []string
		expected int
	}{
		{[]string{"2", "1", "+", "3", "*"}, 9},
		{[]string{"4", "13", "5", "/", "+"}, 6},
		{[]string{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}, 22},
	}

	for _, tc := range testCases {
		actual := evalRPN(tc.tokens)
		if actual != tc.expected {
			t.Errorf("evalRPN(%v) = %d, expected %d", tc.tokens, actual, tc.expected)
		}
	}
}
