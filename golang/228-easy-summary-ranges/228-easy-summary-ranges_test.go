package main

import (
	"reflect"
	"strconv"
	"testing"
)

func summaryRanges(nums []int) []string {
	if len(nums) == 0 {
		return []string{}
	}
	res := []string{}
	start := nums[0]
	prev := nums[0]
	for i := 1; i < len(nums); i++ {
		if prev+1 < nums[i] {
			if start == prev {
				res = append(res, strconv.Itoa(start))
			} else {
				res = append(res, strconv.Itoa(start)+"->"+strconv.Itoa(prev))
			}
			start = nums[i]
		}
		prev = nums[i]
	}
	if start == prev {
		res = append(res, strconv.Itoa(start))
	} else {
		res = append(res, strconv.Itoa(start)+"->"+strconv.Itoa(prev))
	}
	return res
}

func TestSummaryRanges(t *testing.T) {
	testCases := []struct {
		nums     []int
		expected []string
	}{
		{[]int{0, 1, 2, 4, 5, 7}, []string{"0->2", "4->5", "7"}},
		{[]int{0, 2, 3, 4, 6, 8, 9}, []string{"0", "2->4", "6", "8->9"}},
	}

	for _, tc := range testCases {
		actual := summaryRanges(tc.nums)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("summaryRanges(%v) = %v, expected %v", tc.nums, actual, tc.expected)
		}
	}
}
