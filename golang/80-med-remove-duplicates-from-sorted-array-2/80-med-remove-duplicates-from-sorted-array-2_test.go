package main

import (
	"testing"
)

func removeDuplicates(nums []int) int {
	l, r := 0, 0

	for r < len(nums) {
		count := 1
		for r+1 < len(nums) && nums[r] == nums[r+1] {
			r += 1
			count += 1
		}

		iters := 2
		if count < 2 {
			iters = count
		}
		for i := 0; i < iters; i++ {
			nums[l] = nums[r]
			l += 1
		}

		r += 1
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
