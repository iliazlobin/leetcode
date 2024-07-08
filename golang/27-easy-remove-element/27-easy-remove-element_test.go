package main

import (
	"sort"
	"testing"
)

// [3,2,2,3]
// O(n)

func removeElement(nums []int, val int) int {
	if len(nums) == 1 && nums[0] == val {
		return 1
	}
	left, right := 0, len(nums)-1
	count := 0
	for left < right {
		if nums[left] == val {
			for left < right {
				if nums[right] != val {
					nums[left] = nums[right]
					count += 1
					right -= 1
					break
				} else {
					count += 1
				}
				right -= 1
			}
		}
		left += 1
	}
	return len(nums) - count
}

func TestRemoveElement(t *testing.T) {
	testCases := []struct {
		nums         []int
		val          int
		expectedK    int
		expectedNums []int
	}{
		{[]int{3, 2, 2, 3}, 3, 2, []int{2, 2}},
		{[]int{0, 1, 2, 2, 3, 0, 4, 2}, 2, 5, []int{0, 1, 3, 0, 4}},
	}

	for _, tc := range testCases {
		numsCopy := make([]int, len(tc.nums))
		copy(numsCopy, tc.nums)
		k := removeElement(numsCopy, tc.val)
		if k != tc.expectedK {
			t.Errorf("removeElement(%v, %d) = %d, expected %d", tc.nums, tc.val, k, tc.expectedK)
		}

		sort.Ints(numsCopy[:k]) // Sort the first k elements of numsCopy
		for i := 0; i < k; i++ {
			if numsCopy[i] != tc.expectedNums[i] {
				t.Errorf("After removeElement, nums[%d] = %d, expected %d", i, numsCopy[i], tc.expectedNums[i])
			}
		}
	}
}
