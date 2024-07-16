package main

import (
	"testing"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	m -= 1
	n -= 1

	w := len(nums1) - 1
	for n >= 0 {
		if m >= 0 && nums1[m] > nums2[n] {
			nums1[w] = nums1[m]
			m -= 1
		} else {
			nums1[w] = nums2[n]
			n -= 1
		}
		w -= 1
	}
}

func TestMerge(t *testing.T) {
	testCases := []struct {
		nums1    []int
		m        int
		nums2    []int
		n        int
		expected []int
	}{
		{
			nums1:    []int{1, 2, 3, 0, 0, 0},
			m:        3,
			nums2:    []int{2, 5, 6},
			n:        3,
			expected: []int{1, 2, 2, 3, 5, 6},
		},
		{
			nums1:    []int{1},
			m:        1,
			nums2:    []int{},
			n:        0,
			expected: []int{1},
		},
		{
			nums1:    []int{0},
			m:        0,
			nums2:    []int{1},
			n:        1,
			expected: []int{1},
		},
	}

	for _, tc := range testCases {
		merge(tc.nums1, tc.m, tc.nums2, tc.n)
		for i, v := range tc.nums1 {
			if v != tc.expected[i] {
				t.Errorf("merge() failed: expected %v, got %v", tc.expected, tc.nums1)
				break
			}
		}
	}
}
