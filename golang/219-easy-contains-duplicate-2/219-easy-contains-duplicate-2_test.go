package main

import (
	"testing"
)

func containsNearbyDuplicate(nums []int, k int) bool {
	left := 0
	hMap := make(map[int]bool)
	for right := 0; right < len(nums); right++ {
		if _, ok := hMap[nums[right]]; ok {
			return true
		}
		hMap[nums[right]] = true
		if right-left >= k {
			delete(hMap, nums[left])
			left++
		}
	}
	return false
}

func TestContainsNearbyDuplicate(t *testing.T) {
	testCases := []struct {
		nums     []int
		k        int
		expected bool
	}{
		// {[]int{1, 2, 3, 1}, 3, true},
		// {[]int{1, 0, 1, 1}, 1, true},
		{[]int{1, 2, 3, 1, 2, 3}, 2, false},
	}

	for _, tc := range testCases {
		actual := containsNearbyDuplicate(tc.nums, tc.k)
		if actual != tc.expected {
			t.Errorf("containsNearbyDuplicate(%v, %d) = %v, expected %v", tc.nums, tc.k, actual, tc.expected)
		}
	}
}
