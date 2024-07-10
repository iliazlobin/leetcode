package main

import (
	"reflect"
	"sort"
	"testing"
)

func groupAnagrams(strs []string) [][]string {
	hMap := make(map[[26]int][]string)

	for _, s := range strs {
		chars := [26]int{}
		for _, c := range s {
			chars[c-'a'] += 1
		}
		hMap[chars] = append(hMap[chars], s)
	}

	res := [][]string{}
	for _, v := range hMap {
		res = append(res, v)
	}

	return res
}

func TestGroupAnagrams(t *testing.T) {
	testCases := []struct {
		strs     []string
		expected [][]string
	}{
		{
			[]string{"eat", "tea", "tan", "ate", "nat", "bat"},
			[][]string{{"bat"}, {"nat", "tan"}, {"ate", "eat", "tea"}},
		},
		{
			[]string{""},
			[][]string{{""}},
		},
		{
			[]string{"a"},
			[][]string{{"a"}},
		},
		{
			[]string{"bdddddddddd", "bbbbbbbbbbc"},
			[][]string{{"bbbbbbbbbbc"}, {"bdddddddddd"}},
		},
	}

	for _, tc := range testCases {
		actual := groupAnagrams(tc.strs)
		sortSliceOfSlice(actual)
		sortSliceOfSlice(tc.expected)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("groupAnagrams(%v) = %v, expected %v", tc.strs, actual, tc.expected)
		}
	}
}

func sortStringSlice(slice []string) {
	sort.Strings(slice)
}

func sortSliceOfSlice(slice [][]string) {
	for _, innerSlice := range slice {
		sortStringSlice(innerSlice)
	}
	sort.Slice(slice, func(i, j int) bool {
		return slice[i][0] < slice[j][0]
	})
}
