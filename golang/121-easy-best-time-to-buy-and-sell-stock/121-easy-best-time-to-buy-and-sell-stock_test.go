package main

import (
	"math"
	"testing"
)

func maxProfit(prices []int) int {
	globalMin := math.MaxInt32
	maxProfit := 0
	for _, n := range prices {
		if globalMin != math.MaxInt32 && n-globalMin > maxProfit {
			maxProfit = n - globalMin
		}
		if n < globalMin {
			globalMin = n
		}
	}
	return maxProfit
}

func TestMaxProfit(t *testing.T) {
	testCases := []struct {
		prices   []int
		expected int
	}{
		{[]int{7, 1, 5, 3, 6, 4}, 5},
		// {[]int{7, 6, 4, 3, 1}, 0},
	}

	for _, tc := range testCases {
		actual := maxProfit(tc.prices)
		if actual != tc.expected {
			t.Errorf("maxProfit(%v) = %d, expected %d", tc.prices, actual, tc.expected)
		}
	}
}
