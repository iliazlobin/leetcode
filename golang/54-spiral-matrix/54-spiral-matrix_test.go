package main

import (
	"reflect"
	"testing"
)

func spiralOrder(matrix [][]int) []int {
	if len(matrix) == 0 {
		return []int{}
	}

	res := []int{}
	l, r := 0, len(matrix[0])-1
	t, b := 0, len(matrix)-1

	for {
		if l > r {
			break
		}
		for i := l; i <= r; i += 1 {
			res = append(res, matrix[t][i])
		}
		t += 1

		if t > b {
			break
		}
		for j := t; j <= b; j += 1 {
			res = append(res, matrix[j][r])
		}
		r -= 1

		if r < l {
			break
		}
		for i := r; i >= l; i -= 1 {
			res = append(res, matrix[b][i])
		}
		b -= 1

		if b < t {
			break
		}
		for j := b; j >= t; j -= 1 {
			res = append(res, matrix[j][l])
		}
		l += 1
	}

	return res
}

func TestSpiralOrder(t *testing.T) {
	testCases := []struct {
		matrix   [][]int
		expected []int
	}{
		{
			matrix: [][]int{
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9},
			},
			expected: []int{1, 2, 3, 6, 9, 8, 7, 4, 5},
		},
		{
			matrix: [][]int{
				{1, 2, 3, 4},
				{5, 6, 7, 8},
				{9, 10, 11, 12},
			},
			expected: []int{1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7},
		},
	}

	for _, tc := range testCases {
		actual := spiralOrder(tc.matrix)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("spiralOrder(%v) = %v, expected %v", tc.matrix, actual, tc.expected)
		}
	}
}
