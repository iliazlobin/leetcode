package main

import (
	"testing"
)

func canCompleteCircuit(gas []int, cost []int) int {
	gasSum := 0
	for _, g := range gas {
		gasSum += g
	}
	costSum := 0
	for _, c := range cost {
		costSum += c
	}
	if gasSum < costSum {
		return -1
	}

	diffs := make([]int, len(gas))
	for i := 0; i < len(gas); i += 1 {
		diffs[i] = gas[i] - cost[i]
	}

	start := 0
	total := 0
	for i := 0; i < len(gas); i += 1 {
		total = total + diffs[i]
		if total < 0 {
			start = i + 1
			if start == len(gas) {
				start = 0
			}
			total = 0
		}
	}

	return start
}

func TestCanCompleteCircuit(t *testing.T) {
	testCases := []struct {
		gas      []int
		cost     []int
		expected int
	}{
		{
			gas:      []int{1, 2, 3, 4, 5},
			cost:     []int{3, 4, 5, 1, 2},
			expected: 3,
		},
		{
			gas:      []int{2, 3, 4},
			cost:     []int{3, 4, 3},
			expected: -1,
		},
	}

	for _, tc := range testCases {
		actual := canCompleteCircuit(tc.gas, tc.cost)
		if actual != tc.expected {
			t.Errorf("canCompleteCircuit(%v, %v) = %d, expected %d", tc.gas, tc.cost, actual, tc.expected)
		}
	}
}
