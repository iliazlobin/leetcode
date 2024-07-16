package main

import (
	"testing"
)

func removeDuplicates(nums []int) int {
	l, r := 0, 0
	start := 0

	for r < len(nums) {
		for r < len(nums)-1 && nums[r+1] == nums[r] {
			r += 1
		}

		duplicates := r - start + 1

		copies := duplicates
		if copies > 2 {
			copies = 2
		}
		for copies > 0 {
			if start > 0 {
				nums[l] = nums[r]
			}
			l += 1
			copies -= 1
		}

		r += 1
		start = r
	}

	return l
}

func TestRemoveDuplicates(t *testing.T) {
	testCases := []struct {
		nums         []int
		expectedK    int
		expectedNums []int // Expected result after calling the function, only up to expectedK elements are checked
	}{
		{
			nums:         []int{1, 1, 1, 2, 2, 3},
			expectedK:    5,
			expectedNums: []int{1, 1, 2, 2, 3},
		},
		{
			nums:         []int{0, 0, 1, 1, 1, 1, 2, 3, 3},
			expectedK:    7,
			expectedNums: []int{0, 0, 1, 1, 2, 3, 3},
		},
	}

	for _, tc := range testCases {
		k := removeDuplicates(tc.nums)
		if k != tc.expectedK {
			t.Errorf("removeDuplicates() = %v, expected %v", k, tc.expectedK)
		}
		for i := 0; i < tc.expectedK; i++ {
			if tc.nums[i] != tc.expectedNums[i] {
				t.Errorf("After removeDuplicates(), nums[%d] = %v, expected %v", i, tc.nums[i], tc.expectedNums[i])
				break
			}
		}
	}
}
