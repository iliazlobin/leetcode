package main

import (
	"testing"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	i, j := len(nums1)-len(nums2)-1, len(nums2)-1
	p := len(nums1) - 1
	for j >= 0 {
		if i >= 0 && nums1[i] >= nums2[j] {
			nums1[p] = nums1[i]
			i -= 1
		} else {
			nums1[p] = nums2[j]
			j -= 1
		}
		p -= 1
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
		{[]int{1, 2, 3, 0, 0, 0}, 3, []int{2, 5, 6}, 3, []int{1, 2, 2, 3, 5, 6}},
		{[]int{4, 5, 6, 0, 0, 0}, 3, []int{1, 2, 3}, 3, []int{1, 2, 3, 4, 5, 6}},
		{[]int{1}, 1, []int{}, 0, []int{1}},
		{[]int{0}, 0, []int{1}, 1, []int{1}},
	}

	for _, tc := range testCases {
		merge(tc.nums1, tc.m, tc.nums2, tc.n)
		for i, v := range tc.nums1 {
			if v != tc.expected[i] {
				t.Errorf("merge(%v, %d, %v, %d) = %v, expected %v", tc.nums1, tc.m, tc.nums2, tc.n, tc.nums1, tc.expected)
				break
			}
		}
	}
}
