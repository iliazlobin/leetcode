package main

import (
	"testing"
)

func removeDuplicates(nums []int) int {
	left := 1
	for right := 1; right < len(nums); right += 1 {
		if nums[right] != nums[right-1] {
			nums[left] = nums[right]
			left += 1
		}
	}
	return left
}

func TestRemoveDuplicates(t *testing.T) {
	testCases := []struct {
		nums         []int
		expectedK    int
		expectedNums []int
	}{
		{[]int{1, 1, 2}, 2, []int{1, 2}},
		{[]int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}, 5, []int{0, 1, 2, 3, 4}},
	}

	for _, tc := range testCases {
		numsCopy := make([]int, len(tc.nums))
		copy(numsCopy, tc.nums)
		k := removeDuplicates(numsCopy)
		if k != tc.expectedK {
			t.Errorf("removeDuplicates(%v) = %d, expected %d", tc.nums, k, tc.expectedK)
		}

		for i := 0; i < k; i++ {
			if numsCopy[i] != tc.expectedNums[i] {
				t.Errorf("After removeDuplicates, nums[%d] = %d, expected %d", i, numsCopy[i], tc.expectedNums[i])
			}
		}
	}
}
