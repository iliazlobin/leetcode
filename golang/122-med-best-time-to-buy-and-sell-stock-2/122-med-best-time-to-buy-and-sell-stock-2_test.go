package main

import (
	"testing"
)

func maxProfit(prices []int) int {
	profit := 0
	for i, _ := range prices {
		if i < len(prices)-1 && prices[i+1] > prices[i] {
			profit += prices[i+1] - prices[i]
		}
	}
	return profit
}

func TestMaxProfit(t *testing.T) {
	testCases := []struct {
		prices   []int
		expected int
	}{
		{
			prices:   []int{7, 1, 5, 3, 6, 4},
			expected: 7,
		},
		{
			prices:   []int{1, 2, 3, 4, 5},
			expected: 4,
		},
		{
			prices:   []int{7, 6, 4, 3, 1},
			expected: 0,
		},
	}

	for _, tc := range testCases {
		actual := maxProfit(tc.prices)
		if actual != tc.expected {
			t.Errorf("maxProfit(%v) = %d, expected %d", tc.prices, actual, tc.expected)
		}
	}
}
