package main

import (
	"fmt"
	"sort"
)

/*
https://leetcode.com/problems/3sum/
*/
func threeSum(nums []int) [][]int {
	results := [][]int{}
	sort.Ints(nums)
	for i, a := range nums {
		if i > 0 && a == nums[i-1] {
			continue
		}
		l, r := i+1, len(nums)-1
		for l < r {
			sum := a + nums[l] + nums[r]
			if sum == 0 {
				results = append(results, []int{a, nums[l], nums[r]})
				l++
				for nums[l] == nums[l-1] && l < r {
					l++
				}
			} else if sum < 0 {
				l++
			} else if sum > 0 {
				r--
			}
		}
	}
	return results
}

func main() {
	fmt.Println(threeSum([]int{-1, 0, 1, 2, -1, -4}))
	fmt.Println(threeSum([]int{}))
	fmt.Println(threeSum([]int{0}))

}
